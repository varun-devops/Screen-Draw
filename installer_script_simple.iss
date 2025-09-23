#define MyAppName "WebtroopsScreen Draw"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "WebTroop"
#define MyAppURL "https://github.com/varun-devops/Screen-Draw"
#define MyAppExeName "WebtroopsScreen Draw.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
AppId={{F9D7B4E0-8C36-4F3A-B1B8-E9F8E9E9E9E9}
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
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "src\*.py"; DestDir: "{app}\src"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  ConfigPath, ConfigContent: string;
begin
  if CurStep = ssPostInstall then
  begin
    // Create user's config directory
    ConfigPath := ExpandConstant('{userappdata}\ScreenDraw');
    if not DirExists(ConfigPath) then
      CreateDir(ConfigPath);
      
    // Create config file with default hotkey
    ConfigContent := 'hotkey = "ctrl+shift+d"' + #13#10;
    
    // Write config file
    SaveStringToFile(ConfigPath + '\config.ini', ConfigContent, False);
  end;
end;