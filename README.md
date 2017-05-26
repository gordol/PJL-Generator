Usage:

SSID and Encryption Key are required fields.
Encryption type defaults to WPA2, and mode defaults to AES.

generate_commands(ssid, enc_key, enc_type='wpa2', enc_mode='aes')

Output is a PJL text buffer to be sent to the printer.


PJL is "Printer Job Language"

You can find a manual from Brother [here](http://download.brother.com/welcome/docp000487/cv_ql720nw_ruseng_net_0.pdf)(pdf warning).

This is a manual for their GUI network configuration program. In it, they state the ability for that progarm to do the following:

> Saves network settings in PJL format

After doing this, it is then trivial to reverse engineer the file.


I have only tested this on the following printer models: 

 - ql720nw

If you test this and it works on a different model, please let me know. I would imagine network configuration is global across all of Brother's products, but this may not be the case.