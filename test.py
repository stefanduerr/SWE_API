customers = [('Franzl', 'Lang', 'Burggasse_27', '1150', '1993-12-12', 'franzl@gmx.at', 'online'),
                    ('Alex', 'Kurz', 'Burggasse_27', '1150', '1993-12-12', 'Alex@gmx.at', 'away'),
                    ('Mark', 'Huber', 'Burggasse_27', '1150', '1993-12-12', 'Mark@gmx.at', 'offline'),
                    ('Oliver', 'Kahn', 'Burggasse_27', '1150', '1993-12-12', 'Oliver@gmx.at', 'away'),
                    ('Joachim', 'Rhabarber', 'Burggasse_27', '1150', '1993-12-12', 'Joachim@gmx.at', 'offline'),
                    ('Sarah', 'Zichmann', 'Burggasse_27', '1150', '1993-12-12', 'Sarah@gmx.at', 'offline'),
                    ('Annalena', 'Lager', 'Burggasse_27', '1150', '1993-12-12', 'Annalena@gmx.at', 'offline'),
                    ('Maria', 'Robust', 'Burggasse_27', '1150', '1993-12-12', 'Maria@gmx.at', 'online'),
                    ('Hannah', 'Augartner', 'Burggasse_27', '1150', '1993-12-12', 'Hannah@gmx.at', 'online'),
                    ('Julia', 'Legano', 'Burggasse_27', '1150', '1993-12-12', 'Julia@gmx.at', 'away')]
values = ', '.join(map(str, customers))

print("INSERT INTO CUSTOMERS(First_Name, Last_Name, Address, Postal_Code, Date_Of_Birth, Email, Status) VALUES {};".format(values))



