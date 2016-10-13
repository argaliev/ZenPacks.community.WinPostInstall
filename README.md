======================================
ZenPacks.community.WinPostInstall
======================================


Description
===========

ZenPack make post install configuration of templates, thresholds and tranforms for windows ZenPack.

List of changes:
  - turn on all services in mode auto to monitoring
  - exclude `RemoteRegistry, ShellHWDetection, SysmonLog, TapiSrv, clr_optimization, sppsvc` services from monitoring
  - disable `WinSQLJob` monitoring
  - add transform to EventLog event class to drop unnecessary events and downgrade event severity
  - add transform to Memory event class for more convenient message
  - add transform to downgrade severity for some winrm events
  - add custom Device thresholds to memory and cpu load to use `DurationThreshold`
  - add custom FileSystem threshold, that uses CustomProperty `cFileSystemThreshold` with value `<102400?absolute=800:percent=5`.
  
  Syntax mean: if size `< 102400 MB` then use threshold value 800 MB, else use value of 5 persent of disk size.


How to create Custom Property discribed in http://wiki.zenoss.org/Per-Filesystem_Thresholds. Shortly, go by url.
http://ZENOSSSERVER/zport/dmd/Devices/manage, select 'Script(Python)' from drop-list in upper right corner. In id type `getFileSystemThreshold`,
then paste code from `lib/FileSystemThreshold.py`.

Requirements & Dependencies
===========================

    * Zenoss Versions Supported: > 4.0
    * External Dependencies:
    * ZenPack Dependencies:
    * Installation Notes: zenhub and zopectl restart after installing this ZenPack.
    * Configuration:

Installation
============
Normal Installation (packaged egg)
----------------------------------
Copy the downloaded .egg to your Zenoss server and run the following commands as the zenoss
user::

   * zenpack --install <package.egg>
   * zenhub restart
   * zopectl restart

Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to this
ZenPack you should clone the git repository, then install the ZenPack in
developer mode::

   * zenpack --link --install <package>
   * zenhub restart
   * zopectl restart

Configuration
=============

Tested with Zenoss 4.2.5

Monitoring Templates
-----------
- **/Devices/Server/Microsoft/Cluster/rrdTemplates/WinSQLJob**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/clr_optimization_v2.0.50727_32**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/clr_optimization_v2.0.50727_64**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/clr_optimization_v4.0.30319_32**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/clr_optimization_v4.0.30319_64**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/Device**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/FileSystem**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/RemoteRegistry**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/ShellHWDetection**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/sppsvc**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/SysmonLog**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/TapiSrv**
- **/Devices/Server/Microsoft/Windows/rrdTemplates/WinService**


Event Classes
-----------
- **/Events/Perf/Memory**
- **/Events/Status/Winrm**
- **/Events/Status/Winrm/Ping**
- **/Events/Win/EventLog**

