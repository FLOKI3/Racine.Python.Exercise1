day = int(input("Entrer le jour: "))
month = int(input("Entrer le mois: "))
year = int(input("Entrer l'annee: "))

# Months that have 31 days
if month==1 or month==3 or month==5 or month==7 or month==8 or month==12:
    max_days=31
# Months that have 30 days
elif month==4 or month==6 or month==9 or month==11:
    max_days=30

# Leap year in february :
# year%100!=0: هذا الشرط يتحقق إذا لم يكن العام قابلًا للقسمة على 100 بدون باقي
# year%400==0: هذا الشرط يتحقق إذا كان العام قابلًا للقسمة على 400 بدون باقي
# year%4==0  : يتحقق هذا الشرط إذا كان العام قابلًا للقسمة على 4 بدون باقي
elif year%4==0 and year%100!=0 or year%400==0:
    max_days=29
else:
    max_days=28

# Print if is verified or not
if month<1 or month>12:
    print("- La date saisie n'est pas valide")
    print("- Vérifiez la place de mois")
elif year<1:
    print("- La date saisie n'est pas valide")
    print("- Vérifiez la place de l'annee")
elif day<1 or day>max_days:
    print("- La date saisie n'est pas valide")
    print("- Vérifiez la place de jour")
else:
    print("La date saisie est valide \n\nVoila le calendrier de ce mois:\n")

# Calendar tool
import calendar
try:
    print(calendar.month(year,month))
# Calendar Error
except ValueError:
    print("- Veuillez entrer une année et un mois valides.")
except IndexError:
    print("- La date doit être validé pour ouvrir le calendrier.")




