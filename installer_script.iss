
#define MyAppName "WebtroopsScreen Draw"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "WebTroop"
#define MyAppURL "https://github.com/varun-devops/Screen-Draw"
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

[Files]
Source: "dist\WebtroopsScreen Draw.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs
Source: "src\*.py"; DestDir: "{app}\src"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{commonstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startupicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
var
  HotkeyPage: TInputQueryWizardPage;
  HotkeyComboBox: TNewComboBox;

procedure InitializeWizard;
begin
  // Create a custom page for hotkey selection
  HotkeyPage := CreateInputQueryPage(wpSelectTasks,
    'Select Hotkey', 'Choose a hotkey for activating the drawing tool',
    'Select which keyboard shortcut you want to use to activate WebtroopsScreen Draw. This hotkey will work globally, from any application.');
  
  // Create a combobox for hotkey selection
  HotkeyComboBox := TNewComboBox.Create(WizardForm);
  HotkeyComboBox.Parent := HotkeyPage.Surface;
  HotkeyComboBox.Left := ScaleX(8);
  HotkeyComboBox.Top := ScaleY(24);
  HotkeyComboBox.Width := ScaleX(300);
  HotkeyComboBox.Style := csDropDownList;
  
  // Add options to the combobox
  HotkeyComboBox.Items.Add('Ctrl+Alt+W (Default)');
  HotkeyComboBox.Items.Add('F9');
  HotkeyComboBox.Items.Add('F1');
  HotkeyComboBox.Items.Add('F2');
  HotkeyComboBox.Items.Add('F3');
  HotkeyComboBox.Items.Add('F4');
  HotkeyComboBox.Items.Add('F5');
  HotkeyComboBox.Items.Add('F6');
  HotkeyComboBox.Items.Add('F7');
  HotkeyComboBox.Items.Add('F8');
  HotkeyComboBox.Items.Add('F10');
  HotkeyComboBox.Items.Add('F11');
  HotkeyComboBox.Items.Add('F12');
  HotkeyComboBox.Items.Add('Ctrl+Alt+D');
  HotkeyComboBox.Items.Add('Ctrl+Alt+S');
  HotkeyComboBox.Items.Add('Alt+Z');
  HotkeyComboBox.Items.Add('Alt+X');
  HotkeyComboBox.Items.Add('Alt+C');
  
  // Set default selection
  HotkeyComboBox.ItemIndex := 0;
end;

function GetSelectedHotkey(Param: string): string;
var
  SelectedHotkey: string;
begin
  SelectedHotkey := HotkeyComboBox.Text;
  
  // Strip the '(Default)' suffix if present
  if Pos('(Default)', SelectedHotkey) > 0 then
    SelectedHotkey := 'Ctrl+Alt+W';
  
  // Return only the key part, not any explanation
  if Pos(' ', SelectedHotkey) > 0 then
    Result := Copy(SelectedHotkey, 1, Pos(' ', SelectedHotkey) - 1)
  else
    Result := SelectedHotkey;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  SelectedHotkey, ConfigFilePath, ConfigContent: string;
begin
  if CurStep = ssPostInstall then
  begin
    // Get the selected hotkey
    SelectedHotkey := GetSelectedHotkey('');
    
    // Create or update config file
    ConfigFilePath := ExpandConstant('{app}\src\config.py');
    
    // Create config content
    ConfigContent := '"""' + #13#10 + 'Configuration file for WebTroopsScreen Draw' + #13#10 + 
                     'This file is generated during installation.' + #13#10 + '"""' + #13#10 + #13#10 + 
                     '# Hotkey configuration' + #13#10 + 
                     'HOTKEY = "' + SelectedHotkey + '"' + #13#10 + #13#10 + 
                     '# Auto start setting' + #13#10;
    
    if WizardIsTaskSelected('startupicon') then
      ConfigContent := ConfigContent + 'AUTO_START = True' + #13#10
    else
      ConfigContent := ConfigContent + 'AUTO_START = False' + #13#10;
    
    // Write config file
    SaveStringToFile(ConfigFilePath, ConfigContent, False);
  end;
end;
