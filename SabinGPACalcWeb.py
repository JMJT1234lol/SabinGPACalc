from flask import Flask, render_template, request 
app = Flask(__name__)

#Assign Number from  1.0 to 5.0
def ValueAssigner(letter):
    if  letter == "A" or letter == "a":
         return 4.0
    elif letter == "B" or letter == "b":
            return 3.0
    elif letter == "C" or letter == "c":
            return  2.0
    elif letter == "D" or letter == "d":
          return 1.0
    elif letter == "F" or letter == "f":
          return 0.0
    elif letter is None:
          return None 
#Regulars, Honors, or AP 
def ClassAssigner(letter, subject):
    if letter is None:
          return None
    if subject == "Math":
         class_type = request.form.get(f"{subject}_type")
         if class_type:
            class_type = request.form.get(f"{subject}_type")
            print(f"Class type for {subject}: {class_type}")
            if class_type.lower() in ["no", "No", "n", "Regular", "N"]:
             return letter + 0.0
            elif class_type.lower() in ["Yes", "yes", "honors", "Honors", "y", "H"]:
                return letter + 0.5
    return letter
   
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subjects = ["Language Arts", "Social Studies", "Science", "Math", "Elective One", "Elective Two"]
        grades = []
        failing_count = 0
        for subject in subjects:
            grade = request.form.get(subject)
            print(f"Grade for {subject}: {grade}")
            grade = ValueAssigner(grade)
            print(f"Assigned value for {subject}: {grade}")
            grade = ClassAssigner(grade, subject)
            print(f"Adjusted value for {subject}: {grade}")
            grades.append(grade)
            if grade <= 1.5:
                failing_count += 1
            

        grades = [value for value in grades if value is not None]
        print(f"Filtered grades: {grades}")
        ValuesAdded = sum(grades)
        GPA = (ValuesAdded / len(grades))
        GPA = round(GPA, 1)
        
        print("Your GPA is: " + str(GPA))
        if GPA >= 4.0:
            honor_roll = "Principal's Honor Roll"
        elif GPA >= 3.0:
            honor_roll = "Honors Roll"
        else:
            honor_roll = "No Honor Roll"
        return render_template('index.html', gpa=GPA, honor_roll=honor_roll, failing_count=failing_count)
    return render_template('index.html', gpa=None, honor_roll=None, failing_count=None)
if __name__ == '__main__':
     app.run(debug=True)


