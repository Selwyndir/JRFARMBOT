<?php

//Initialisation X
 if(($_POST['executer'] == 'Init_X'))
 { exec('sudo python3 /var/www/html/python/initialisation_X.py'); }

//Initialisation Y
 if(($_POST['executer'] == 'Init_Y'))
 { exec('sudo python3 /var/www/html/python/initialisation_Y.py'); }
 
 //Initialisation Z
 if(($_POST['executer'] == 'Init_Z'))
 { exec('sudo python3 /var/www/html/python/initialisation_Z.py'); }

//Mesure humidite
 if(($_POST['executer'] == 'humidite'))
 { exec('sudo python3 /var/www/html/python/humidite.py'); }

//Arrosage
 if(($_POST['executer'] == 'arrosage'))
 { exec('sudo python3 /var/www/html/python/arrosage.py'); }

//Lumiere ON
 if(($_POST['executer'] == 'LON'))
 { exec('sudo python3 /var/www/html/python/lumiere_ON.py'); 
 header('Location: mode_m.html');exit(0);}

//Lumiere OFF
 if(($_POST['executer'] == 'LOFF'))
 { exec('sudo python3 /var/www/html/python/lumiere_OFF.py'); }

//Deplacement X+
 if(($_POST['executer'] == 'Xp'))
 { exec('sudo python3 /var/www/html/python/X_plus.py');
    header('Location: mode_m.html');exit(0); }

//Deplacement X-
 if(($_POST['executer'] == 'Xm'))
 { exec('sudo python3 /var/www/html/python/X_moins.py');
header('Location: mode_m.html');exit(0); }

//Deplacement Y+
 if(($_POST['executer'] == 'Yp'))
 { exec('sudo python3 /var/www/html/python/Y_plus.py');
header('Location: mode_m.html');exit(0); }

//Deplacement Y-
 if(($_POST['executer'] == 'Ym'))
 { exec('sudo python3 /var/www/html/python/Y_moins.py');
header('Location: mode_m.html');exit(0); }

//Deplacement Z+
 if(($_POST['executer'] == 'Zp'))
 { exec('sudo python3 /var/www/html/python/Z_plus.py');
header('Location: mode_m.html');exit(0); }

//Deplacement Z-
 if(($_POST['executer'] == 'Zm'))
 { exec('sudo python3 /var/www/html/python/Z_moins.py');
header('Location: mode_m.html');exit(0); }

//Desherbage ON
 if(($_POST['executer'] == 'desherbage_ON'))
 { exec('sudo python3 /var/www/html/python/desherbage_ON.py');
header('Location: mode_m.html');exit(0); }

//Desherbage OFF
 if(($_POST['executer'] == 'desherbage_OFF'))
 { exec('sudo python3 /var/www/html/python/desherbage_OFF.py');
header('Location: mode_m.html');exit(0); }

//Aspiration ON
 if(($_POST['executer'] == 'aspiration_ON'))
 { exec('sudo python3 /var/www/html/python/aspiration_ON.py');
header('Location: mode_m.html');exit(0); }

//Aspiration OFF
 if(($_POST['executer'] == 'aspiration_OFF'))
 { exec('sudo python3 /var/www/html/python/aspiration_OFF.py');
header('Location: mode_m.html');exit(0); }

//Ranger Outil n°1
 if(($_POST['executer'] == 'ranger_outil_1'))
 { exec('sudo python3 /var/www/html/python/ranger_outil_1.py');
header('Location: mode_m.html');exit(0); }

//Prendre Outil n°1
 if(($_POST['executer'] == 'prendre_outil_1'))
 { exec('sudo python3 /var/www/html/python/prendre_outil_1.py');
header('Location: mode_m.html');exit(0); }

//Prendre une photo
 if(($_POST['executer'] == 'Photo'))
 { exec('sudo python3 /var/www/html/python/photo.py'); }

//Point P1
 if(($_POST['executer'] == '01'))
 { exec('sudo python3 /var/www/html/python/P1.py'); }

//Point P2
 if(($_POST['executer'] == '02'))
 { exec('sudo python3 /var/www/html/python/P2.py'); }

//Point P3
 if(($_POST['executer'] == '03'))
 { exec('sudo python3 /var/www/html/python/P3.py'); }

//Point P4
 if(($_POST['executer'] == '04'))
 { exec('sudo python3 /var/www/html/python/P4.py'); }

//Point P5
 if(($_POST['executer'] == '05'))
 { exec('sudo python3 /var/www/html/python/P5.py'); }

//Point P6
 if(($_POST['executer'] == '06'))
 { exec('sudo python3 /var/www/html/python/P6.py'); }

//Point P7
 if(($_POST['executer'] == '07'))
 { exec('sudo python3 /var/www/html/python/P7.py'); }

//Point P8
 if(($_POST['executer'] == '08'))
 { exec('sudo python3 /var/www/html/python/P8.py'); }

//Point P9
 if(($_POST['executer'] == '09'))
 { exec('sudo python3 /var/www/html/python/P9.py'); }

//Point P10
 if(($_POST['executer'] == '10'))
 { exec('sudo python3 /var/www/html/python/P10.py'); }

//Point P11
 if(($_POST['executer'] == '11'))
 { exec('sudo python3 /var/www/html/python/P11.py'); }

//Point P12
 if(($_POST['executer'] == '12'))
 { exec('sudo python3 /var/www/html/python/P12.py'); }

//Point P13
 if(($_POST['executer'] == '13'))
 { exec('sudo python3 /var/www/html/python/P13.py'); }

//Point P14
 if(($_POST['executer'] == '14'))
 { exec('sudo python3 /var/www/html/python/P14.py'); }

//Point P15
 if(($_POST['executer'] == '15'))
 { exec('sudo python3 /var/www/html/python/P15.py'); }
 
//Automatisation
 if(($_POST['executer'] == 'Automatisation'))
 { exec('sudo python3 /var/www/html/python/Automatisation.php'); }

header('Location: mode_a.html');
 ?>