import os

#لیست ذخیره کردن دانش آموزان
student_score = {}

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                name = parts[0]
                scores_str = parts[1].split(",")
                scores = [float(score) for score in scores_str]
                student_score[name] = scores
except FileNotFoundError:
    pass  # اگر فایل نبود، یعنی بار اولی که اجرا می‌شه

#افزودن دانش آموز به لیست
def add_student():

    scores = []

    name = input("Enter ful name for Add student:").strip().title()

    
    #حلقه برای دریافت 3 تا نمره و اضافه کردن به یک لیست و اضافه کردن ان به عنوان مقدار دیکشنری به لیست دانش اموزان
    try:
        for _ in range(3):

            score = float(input("Enter score for add student:"))

            scores.append(score)

        if name not in student_score:
            student_score[name] = scores
    
        else:

            return "Do not enter duplicates!"
    
    except ValueError:

        return "Enter score not enter"
    
    with open("students.txt", "a", encoding="utf-8") as file:
        score_line = ",".join([str(score) for score in scores])
        file.write(f"{name}:{score_line}\n")




#نمایش دانش آموزان ذخیره شده
def show_students_score():

    if not student_score:

        return "Student not find!"

    for name , score in student_score.items():

        print(f"{name}: {score}")
        
        


#دریافت میانگین نمرات دانش آموزان
def average_score():

    name_for_average = input("Enter name for average: ").strip().title()

    try:

        for student in student_score:

            # دیکشنری فعلی رو بررسی می‌کنیم
            if name_for_average in student:

                scores = student_score[name_for_average]

                if len(scores) == 0:
                    return ("No score recorded!")
                

                numeric_scores = [float(score) for score in scores]

                average = sum(numeric_scores) / len(numeric_scores)

                return f"The average score of {name_for_average} is: {average:.2f}"

        #اگر اسم موجود نبود
        return "Student not found!"
    
    except KeyError:

        return f"Studet {name_for_average} not found!"
    

#تابع سرچ در لیست دانش اموزان
def search_student():

    #برای دریافت اسم دانش آموز
    name_for_search = input("Enter name for search student:").strip().title()

    #حلقه برای پیدا کردن اسم دریافت شده در لیست
    try:

        for student_name in student_score:

            #اگر اسم در لیست بود نمراتش رو نمایش بده
            if name_for_search in student_name:

                scores_for_search = student_score[name_for_search]

                return f"Student found! Scores: {scores_for_search}"
        
            #اگر نبود ارور نمیده و راهنمایی میکنه
            else:

                return "Student is not find!"
            
    except KeyError:

        return f"Student {name_for_search} not find!"

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


#برای اینکه برنامه تا موقعی که بازه ادامه داشته باشه و هر بار بعدد از هر کاری دوباره گزینه هارو نمایش بده
while True:

    print("__________________________ \n For add student enter: (1) \n For show student score enetr: (2) \n For give avrage score enetr: (3) \n For search in student list enetr: (4) \n For exit enetr: (5) \n __________________________")

    choice = input("Enter option:")

    #صدا زدن تابع افزودن دانش آموز با کد 
    if choice == "1":

        clear_screen()

        add_student()
    
    #برای صدا زدن تابع دیدن لیست دانش آموزان
    elif choice == "2":

        clear_screen()

        print(show_students_score())
    
    #برای صدا زدن تابع میانگین گرفتن از نمرات
    elif choice == "3":

        clear_screen()

        print(average_score())

    #برای صدا خارج شدن از برنامه
    elif choice == "4":

        clear_screen()

        print(search_student())

    #برای سرچ در لیست دانش آموزان
    elif choice == "5":

        clear_screen()

        print("The program has been closed and the information will be deleted. Hope to see you again!")
        break

    else:

        clear_screen()

        print("Invalid option!")