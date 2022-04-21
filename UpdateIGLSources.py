"""
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""

import obspython as obs
import configparser


config = configparser.ConfigParser()

__author__ = "Brambo"
__license__ = "MIT"

bs_ini = ""
browser_ini_path = ""
update_scenes = ""

# ------------------------------------------------------------

def update_url():
    global update_scenes

    #Scene - Scene code - Series _ then find the variables to update
    #for each scene, get a list of browser sources, for each browser source, if it has the scene code
    #then update it based on whether it's a logo, card, roster, record, or TD, or game type

    obs.timer_remove(update_url)
    print("Updated Scenes: " + update_scenes[0])
    for code in update_scenes:
        print("getting sources")
        scene_bsources = []
        scene_tsources = []
        print("Scene name: " + str(code))
        sources = obs.obs_enum_sources()
        if sources is not None:
            for source in sources:
                source_id = obs.obs_source_get_unversioned_id(source)
                if source_id == "browser_source":
                    name = obs.obs_source_get_name(source)
                    
                    if  str(code).lower() in str(name).lower():
                        print("Source name: " + name)
                        print("match")
                        scene_bsources.append(name)
                if source_id == "text_gdiplus":
                    name = obs.obs_source_get_name(source)
                    
                    if  str(code).lower() in str(name).lower():
                        print("Source name: " + name)
                        print("match")
                        scene_tsources.append(name)
                
                obs.obs_source_release(source)                        
        
        
        if len(scene_bsources) > 0:
            print("updating browser sources")
            for scene_bsource in scene_bsources:
                split_depth = len(str(scene_bsource).split("_"))
                series = str(scene_bsource).split("_")[1]
                if split_depth == 4:
                    element = str(scene_bsource).split("_")[3]

                else:
                    element = str(scene_bsource).split("_")[2]

                
                current = obs.obs_get_source_by_name(scene_bsource)
                current_name = obs.obs_source_get_name(current)
                print(str(current_name))
                if "teama" in str(current_name).lower:
                    variable_name = str(series+"ta_"+element).lower()
                    try:
                        if not config['DEFAULT'][variable_name] == "":
                            print(config['DEFAULT'][variable_name])
                            settings = obs.obs_data_create()
                            obs.obs_data_set_string(settings, "url", config['DEFAULT'][variable_name])
                            obs.obs_source_update(current, settings)
                            obs.obs_data_release(settings)
                            
                    except: 
                        print("fail")
                    finally:
                        obs.obs_source_release(current)

                elif "teamb" in str(current_name).lower:
                    variable_name = str(series+"tb_"+element).lower()
                    try:
                        if not config['DEFAULT'][variable_name] == "":
                            print(config['DEFAULT'][variable_name])
                            settings = obs.obs_data_create()
                            obs.obs_data_set_string(settings, "url", config['DEFAULT'][variable_name])
                            obs.obs_source_update(current, settings)
                            obs.obs_data_release(settings)
                            
                    except: 
                        print("fail")
                    finally:
                        obs.obs_source_release(current)
                    
                                        
                else:
                    variable_name = str(series+element).lower()
                    try:
                        if not config['DEFAULT'][variable_name] == "":
                            print(config['DEFAULT'][variable_name])
                            settings = obs.obs_data_create()
                            obs.obs_data_set_string(settings, "url", config['DEFAULT'][variable_name])
                            obs.obs_source_update(current, settings)
                            obs.obs_data_release(settings)
                            
                    except: 
                        print("fail")
                    finally:
                        obs.obs_source_release(current)

        if len(scene_tsources) > 0:
            print("updating text sources")
            for scene_tsource in scene_tsources:
                split_depth = len(str(scene_tsource).split("_"))
                series = str(scene_tsource).split("_")[1]
                if split_depth == 4:
                    element = str(scene_tsource).split("_")[3]

                else:
                    element = str(scene_tsource).split("_")[2]

                
                current = obs.obs_get_source_by_name(scene_tsource)
                current_name = obs.obs_source_get_name(current)
                print(str(current_name))
                if "teama" in str(current_name).lower:
                    variable_name = str(series+"ta_"+element).lower()
                    try:
                        if not config['DEFAULT'][variable_name] == "":
                            settings = obs.obs_data_create()
                            print(config['DEFAULT'][variable_name])
                            obs.obs_data_set_string(settings, "text", config['DEFAULT'][variable_name])
                            obs.obs_source_update(current, settings)
                            obs.obs_data_release(settings)
                            
                    except:
                        print("fail")
                    finally:
                        obs.obs_source_release(current)
                
                elif "teamb" in str(current_name).lower:
                    variable_name = str(series+"tb_"+element).lower()
                    try:
                        if not config['DEFAULT'][variable_name] == "":
                            settings = obs.obs_data_create()
                            print(config['DEFAULT'][variable_name])
                            obs.obs_data_set_string(settings, "text", config['DEFAULT'][variable_name])
                            obs.obs_source_update(current, settings)
                            obs.obs_data_release(settings)
                            
                    except:
                        print("fail")
                    finally:
                        obs.obs_source_release(current)
                else:
                    variable_name = str(series+element).lower()
                    try:
                        if not config['DEFAULT'][variable_name] == "":
                            settings = obs.obs_data_create()
                            print(config['DEFAULT'][variable_name])
                            obs.obs_data_set_string(settings, "text", config['DEFAULT'][variable_name])
                            obs.obs_source_update(current, settings)
                            obs.obs_data_release(settings)
                            
                    except:
                        print("fail")
                    finally:
                        obs.obs_source_release(current)

                
                    
    
    # for code in update_scenes:
    #     scene_sources = []
    #     if sources is not None:
    #         for source in sources:
    #             source_id = obs.obs_source_get_unversioned_id(source)
    #             if source_id == "text_gdiplus":
    #                 name = obs.obs_source_get_name(source)
                    
    #                 if  str(code).lower() in str(name).lower():
    #                     print("Source name: " + name)
    #                     print("match")
    #                     scene_sources.append(name)

    #             obs.obs_source_release(source)  

        

                

    print("done")

def refresh_pressed(props, prop):
    print("Refresh pressed")
    update_url()

# ------------------------------------------------------------

def script_description():
    return "Updates the browser sources used for IGL Casting \n\nby @thebrambo23"

def script_update(settings):
    global browser_ini_path
    global update_scenes
    
    update_scenes = []
    full_codes = obs.obs_data_get_string(settings,"scene_code")
    for code in str(full_codes).split(","):
        update_scenes.append(code)
    browser_ini_path  = obs.obs_data_get_string(settings, "bs_ini")

    config.read(browser_ini_path)

def script_properties():
    props = obs.obs_properties_create()
    
    obs.obs_properties_add_text(props, "bs_ini", "Browser Source INI File", obs.OBS_TEXT_DEFAULT)
    #obs.obs_properties_add_editable_list(props, "scene_code", "Scene Code", obs.OBS_EDITABLE_LIST_TYPE_STRINGS,None,"C:\\")
    obs.obs_properties_add_text(props, 'scene_code', "Scene Codes (seprate by ,)", obs.OBS_TEXT_DEFAULT)


    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
    return props