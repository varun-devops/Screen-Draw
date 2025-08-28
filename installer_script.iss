
#define MyAppName "WebtroopsScreen Draw"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "WebTroop"
#define MyAppURL "https://github.com/varun-devops/WebTroopScreenDraw"
#define MyAppExeName "WebtroopsScreen Draw.exe"

[Setup]
AppId={{F9D7B4E0-8C36-4F3A-B1B8-E9F8E9E9E9E9}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppPublisher}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename={#MyAppName}_Setup_{#MyAppVersion}
; Removed SetupIconFile to avoid icon size issue
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "startmenuicon"; Description: "Create Start Menu shortcuts"; GroupDescription: "{cm:AdditionalIcons}";
Name: "startupicon"; Description: "Start automatically with Windows"; GroupDescription: "Startup";
Name: "registerhotkey"; Description: "Register global hotkey (F9)"; GroupDescription: "Options";

[Files]
Source: "dist\WebtroopsScreen Draw.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{commonstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startupicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
