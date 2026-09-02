#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <title> <message>\n", argv[0]);
        return 1;
    }

    char command[1024];
    // Formats a Toast notification via PowerShell
    snprintf(command, sizeof(command), 
        "powershell -Command \"[reflection.assembly]::loadwithpartialname('System.Windows.Forms'); "
        "$notify = New-Object System.Windows.Forms.NotifyIcon; "
        "$notify.Icon = [System.Drawing.SystemIcons]::Information; "
        "$notify.Visible = $true; "
        "$notify.ShowBalloonTip(3000, '%s', '%s', [System.Windows.Forms.ToolTipIcon]::Info)\"", 
        argv[1], argv[2]);

    return system(command);
}