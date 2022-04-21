# UpdateIGLSources
Python script used to update browser and text sources on OBS

## Description

* *Youtube video with visual instructions will be uploaded soon*

Have you used the IGL Caster urls for your stream but get tired of having to go to all those browser sources and update the URL all the time?  Me too and I only did it for a week.  That's why I developed this Python script that will update all of those text and browser sources for you.  

This will take some modification to your current setup to conform to the script but I promise it will be worth your while.

## How does it work?

First, make sure you install Python 3.6 on your computer, then when you click on the Scripts tab, make sure you point the Python path to that 3.6 version.

Secondly, load the script then point it to the INI file (which it will use to read the information to upload) and the Scene Codes.

Refresh and it will update the specific browser sources with that code.

## Required Source Name formula

This does require a specific forumla in order to work

`<SceneCode>_S<series number>_TeamA(or TeamB)_<source type>`
or
`<SceneCode>_S<series number>_<source type>`

 Example would be:
 
 `RLO_S1_TeamA_Card`
 
 or
 
 `RLO_S2_GameText`
 
 The important thing is the source type matches the type in the INI file
 
 
 **INI Example**
 
`S2TB_Roster:https://www.indygamingleague.com/assets/team/6208849a39f6b000165bb464/roster`
`S2TB_Logo:https://www.indygamingleague.com/assets/general/teamlogo/6208849a39f6b000165bb464`

`S2GT:Standard 3v3`


This might take a bit to work through and setup, but if you do it will save you a lot of time setting up your streams.  I know it already has for mine.
