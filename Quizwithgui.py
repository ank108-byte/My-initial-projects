import sys
import random
from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout,QLineEdit,QApplication,QRadioButton,QMessageBox,QHBoxLayout
from PyQt5.QtCore import Qt
class Quiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz by Anuj!")
        self.nameandsubmit=QLineEdit(self)
        self.nameandsubmit.setPlaceholderText("Enter your name and submit below :")
        self.submitbutton=QPushButton("Submit",self)
        self.label1=QLabel(self)
        self.label2=QLabel(self)
        self.generalrbutton=QRadioButton("General Knowledge",self)
        self.whrbutton=QRadioButton("World's History",self)
        self.nhrbutton=QRadioButton("Nepal's History",self)
        self.sciencerbutton=QRadioButton("Science",self)
        self.question_label=QLabel(self)
        self.option1=QPushButton(self)
        self.option2=QPushButton(self)
        self.option3=QPushButton(self)
        self.option4=QPushButton(self)
        self.correct_ans=QLabel(self)
        self.nextquestion=QPushButton("Next Question",self)
        self.exitcategory=QPushButton("Exit this category")
        self.endquiz=QPushButton("End Quiz",self)
        self.endquizlabel1=QLabel(self)
        self.endquizlabel2=QLabel(self)
        self.overquestions1=QLabel(self)
        self.overquestions2=QLabel(self)
        self.question_label.hide()
        self.option1.hide()
        self.option2.hide()
        self.option3.hide()
        self.option4.hide()
        self.generalrbutton.hide()
        self.whrbutton.hide()
        self.nhrbutton.hide()
        self.sciencerbutton.hide()
        self.nextquestion.hide()
        self.exitcategory.hide()
        self.endquiz.hide()
        self.endquizlabel1.hide()
        self.endquizlabel2.hide()
        self.overquestions1.hide()
        self.overquestions2.hide()
        self.score=0
        self.stored_question=[]
        self.totalquestions=0
        self.initUI()
    def initUI(self):
        vbox=QVBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        hbox3=QHBoxLayout()
        vbox.addWidget(self.nameandsubmit)
        vbox.addWidget(self.submitbutton)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addSpacing(15)
        vbox.addWidget(self.generalrbutton)
        vbox.addWidget(self.whrbutton)
        vbox.addWidget(self.nhrbutton)
        vbox.addWidget(self.sciencerbutton)
        vbox.addWidget(self.question_label)
        hbox1.addWidget(self.option1)
        hbox1.addWidget(self.option2)
        hbox2.addWidget(self.option3)
        hbox2.addWidget(self.option4)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addSpacing(20)
        vbox.addWidget(self.overquestions1)
        vbox.addWidget(self.overquestions2)
        vbox.addWidget(self.correct_ans)
        hbox3.addWidget(self.nextquestion)
        hbox3.addWidget(self.exitcategory)
        hbox3.addWidget(self.endquiz)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.endquizlabel1)
        vbox.addWidget(self.endquizlabel2)
        vbox.setAlignment(Qt.AlignTop)
        self.setLayout(vbox)
        self.question_label.setStyleSheet("font-size:25px;")
        self.correct_ans.setStyleSheet("font-size:30px;")
        self.setStyleSheet("""QPushButton{ font-size:30px;
                                            }
                          """
                           """QRadioButton{font-size:25px;}""")
        self.submitbutton.setStyleSheet("font-size:25px;")
        self.nameandsubmit.setStyleSheet("font-size:25px;")
        self.label1.setStyleSheet("font-size:25px;")
        self.label2.setStyleSheet("font-size:25px;")
        self.option1.setMinimumSize(300, 70)
        self.option2.setMinimumSize(300, 70)
        self.option3.setMinimumSize(300, 70)
        self.option4.setMinimumSize(300, 70)
        self.nextquestion.setStyleSheet("font-size:25px;")
        self.exitcategory.setStyleSheet("font-size:25px;")
        self.endquiz.setStyleSheet("font-size:25px;")
        self.endquizlabel1.setStyleSheet("font-size:30px;" 
                                         "color:hsl(0, 75%, 55%);")
        self.endquizlabel2.setStyleSheet("font-size:30px;"
                                         "color:hsl(0, 75%, 55%);")
        self.overquestions1.setStyleSheet("font-size:25px;")
        self.overquestions2.setStyleSheet("font-size:25px;")
        self.submitbutton.clicked.connect(self.check_validity)
        self.generalrbutton.clicked.connect(self.general_knowledge)
        self.whrbutton.clicked.connect(self.worlds_history)
        self.nhrbutton.clicked.connect(self.nepals_history)
        self.sciencerbutton.clicked.connect(self.science_quiz)
        self.endquiz.clicked.connect(self.end_quiz)
        self.option1.clicked.connect(self.check_answer)
        self.option2.clicked.connect(self.check_answer)
        self.option3.clicked.connect(self.check_answer)
        self.option4.clicked.connect(self.check_answer)
        self.exitcategory.clicked.connect(self.exit_category)
        self.nextquestion.clicked.connect(self.next_question)
    def check_validity(self):
        name=self.nameandsubmit.text().strip()
        self.name=name
        if not name:
            QMessageBox.warning(self,"Invalid name","Please enter your name.")
            return
        if len(name)>50:
            QMessageBox.warning(self,"Invalid name","Your name is too long.")
            return
        if not all(char.isalpha() or char in " -'" for char in name):
            QMessageBox.warning(self,"Invalid name","Name can only contain letters, spaces, hyphens and apostrophes.")
            return
        self.submit_click()
    def submit_click(self):
        self.nameandsubmit.hide()
        self.submitbutton.hide()
        self.label1.setText(f"Hello {self.name}, lets play quiz.")
        self.label2.setText("Select a genre of questions you want to face:")
        self.generalrbutton.show()
        self.whrbutton.show()
        self.nhrbutton.show()
        self.sciencerbutton.show()
    def general_knowledge(self):
        self.option1.setStyleSheet("")
        self.option2.setStyleSheet("")
        self.option3.setStyleSheet("")
        self.option4.setStyleSheet("")
        self.option1.setEnabled(True)
        self.option2.setEnabled(True)
        self.option3.setEnabled(True)
        self.option4.setEnabled(True)
        self.generalrbutton.hide()
        self.whrbutton.hide()
        self.nhrbutton.hide()
        self.sciencerbutton.hide()
        self.label1.hide()
        self.label2.hide()
        self.question_label.show()
        self.option1.show()
        self.option2.show()
        self.option3.show()
        self.option4.show()
        general_questions = [
                            (
                                "What is the largest planet in our Solar System?",
                                ("Earth", "Jupiter", "Saturn", "Neptune"),
                                "Jupiter"
                            ),
                            (
                                "Who painted the Mona Lisa?",
                                ("Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"),
                                "Leonardo da Vinci"
                            ),
                            (
                                "What is the capital city of Australia?",
                                ("Sydney", "Melbourne", "Perth", "Canberra"),
                                "Canberra"
                            ),
                            (
                                "How many continents are there on Earth?",
                                ("5", "6", "7", "8"),
                                "7"
                            ),
                            (
                                "Which is the largest ocean on Earth?",
                                ("Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"),
                                "Pacific Ocean"
                            )
                            ]
        self.unused_questions = []
        for q in general_questions:
            if q[0] not in self.stored_question:
                self.unused_questions.append(q)
        if self.unused_questions==[]:
            self.over_questions()
            return
        question=random.choice(self.unused_questions)
        question_text,options,ans=question
        self.stored_question.append(question_text)
        self.ans=ans
        self.question_label.setText(question_text)
        self.option1.setText(options[0])
        self.option2.setText(options[1])
        self.option3.setText(options[2])
        self.option4.setText(options[3])
    def worlds_history(self):
            self.option1.setStyleSheet("")
            self.option2.setStyleSheet("")
            self.option3.setStyleSheet("")
            self.option4.setStyleSheet("")
            self.option1.setEnabled(True)
            self.option2.setEnabled(True)
            self.option3.setEnabled(True)
            self.option4.setEnabled(True)
            self.generalrbutton.hide()
            self.whrbutton.hide()
            self.nhrbutton.hide()
            self.sciencerbutton.hide()
            self.label1.hide()
            self.label2.hide()
            self.question_label.show()
            self.option1.show()
            self.option2.show()
            self.option3.show()
            self.option4.show()
            world_history_questions =[
                                        (
                                            "Who was the first emperor of the Roman Empire?",
                                            ("Julius Caesar", "Augustus", "Nero", "Constantine"),
                                            "Augustus"
                                        ),
                                        (
                                            "In which year did World War II end?",
                                            ("1943", "1944", "1945", "1946"),
                                            "1945"
                                        ),
                                        (
                                            "Who was known as the 'Maid of Orléans'?",
                                            ("Joan of Arc", "Cleopatra", "Marie Curie", "Catherine the Great"),
                                            "Joan of Arc"
                                        ),
                                        (
                                            "Which ancient civilization built Machu Picchu?",
                                            ("Roman", "Egyptian", "Inca", "Greek"),
                                            "Inca"
                                        ),
                                        (
                                            "The French Revolution began in which year?",
                                            ("1776", "1789", "1799", "1812"),
                                            "1789"
                                        )
                                    ]
            self.unused_questions = []
            for q in world_history_questions:
                if q[0] not in self.stored_question:
                    self.unused_questions.append(q)
            if self.unused_questions==[]:
                    self.over_questions()
                    return
            question=random.choice(self.unused_questions)
            question_text,options,ans=question
            self.stored_question.append(question_text)
            self.ans=ans
            self.question_label.setText(question_text)
            self.option1.setText(options[0])
            self.option2.setText(options[1])
            self.option3.setText(options[2])
            self.option4.setText(options[3])
    def nepals_history(self):
            self.option1.setStyleSheet("")
            self.option2.setStyleSheet("")
            self.option3.setStyleSheet("")
            self.option4.setStyleSheet("")
            self.option1.setEnabled(True)
            self.option2.setEnabled(True)
            self.option3.setEnabled(True)
            self.option4.setEnabled(True)
            self.generalrbutton.hide()
            self.whrbutton.hide()
            self.nhrbutton.hide()
            self.sciencerbutton.hide()
            self.label1.hide()
            self.label2.hide()
            self.question_label.show()
            self.option1.show()
            self.option2.show()
            self.option3.show()
            self.option4.show()
            nepal_history_questions = [
                                            (
                                                "Who is traditionally regarded as the founder of modern Nepal?",
                                                ("Prithvi Narayan Shah", "Jung Bahadur Rana", "Tribhuvan", "Bhimsen Thapa"),
                                                "Prithvi Narayan Shah"
                                            ),
                                            (
                                                "Which dynasty ruled Nepal before the Shah dynasty?",
                                                ("Malla dynasty", "Rana dynasty", "Kirat dynasty", "Licchavi dynasty"),
                                                "Malla dynasty"
                                            ),
                                            (
                                                "Who was the first elected Prime Minister of Nepal?",
                                                ("B. P. Koirala", "Matrika Prasad Koirala", "Tanka Prasad Acharya", "Pushpa Lal Shrestha"),
                                                "B. P. Koirala"
                                            ),
                                            (
                                                "In which year was the Rana regime overthrown?",
                                                ("1947", "1950", "1951", "1955"),
                                                "1951"
                                            ),
                                            (
                                                "Who was known as the 'Light of Asia' and was born in Lumbini?",
                                                ("King Janak", "Gautama Buddha", "Prithvi Narayan Shah", "Araniko"),
                                                "Gautama Buddha"
                                            )
                                       ]
            self.unused_questions = []
            for q in nepal_history_questions:
                if q[0] not in self.stored_question:
                    self.unused_questions.append(q)
            if self.unused_questions==[]:
                    self.over_questions()
                    return
            question=random.choice(self.unused_questions)
            question_text,options,ans=question
            self.stored_question.append(question_text)
            self.ans=ans
            self.question_label.setText(question_text)
            self.option1.setText(options[0])
            self.option2.setText(options[1])
            self.option3.setText(options[2])
            self.option4.setText(options[3])
    def science_quiz(self):
            self.option1.setStyleSheet("")
            self.option2.setStyleSheet("")
            self.option3.setStyleSheet("")
            self.option4.setStyleSheet("")
            self.option1.setEnabled(True)
            self.option2.setEnabled(True)
            self.option3.setEnabled(True)
            self.option4.setEnabled(True)
            self.generalrbutton.hide()
            self.whrbutton.hide()
            self.nhrbutton.hide()
            self.sciencerbutton.hide()
            self.label1.hide()
            self.label2.hide()
            self.question_label.show()
            self.option1.show()
            self.option2.show()
            self.option3.show()
            self.option4.show()
            science_questions = [
                                    (
                                        "What is the chemical symbol for gold?",
                                        ("Ag", "Au", "Fe", "Cu"),
                                        "Au"
                                    ),
                                    (
                                        "What is the largest organ in the human body?",
                                        ("Heart", "Liver", "Skin", "Lungs"),
                                        "Skin"
                                    ),
                                    (
                                        "Which planet is known as the Red Planet?",
                                        ("Venus", "Mars", "Jupiter", "Mercury"),
                                        "Mars"
                                    ),
                                    (
                                        "What is the process by which plants convert light energy into chemical energy?",
                                        ("Respiration", "Photosynthesis", "Transpiration", "Digestion"),
                                        "Photosynthesis"
                                    ),
                                    (
                                        "What is the speed of light in a vacuum approximately?",
                                        ("300,000 km/s", "150,000 km/s", "30,000 km/s", "3,000 km/s"),
                                        "300,000 km/s"
                                    )
                                ]
            self.unused_questions = []
            for q in science_questions:
                if q[0] not in self.stored_question:
                    self.unused_questions.append(q)
            if self.unused_questions==[]:
                self.over_questions()
                return
            question=random.choice(self.unused_questions)
            question_text,options,ans=question
            self.stored_question.append(question_text)
            self.ans=ans
            self.question_label.setText(question_text)
            self.option1.setText(options[0])
            self.option2.setText(options[1])
            self.option3.setText(options[2])
            self.option4.setText(options[3])
    def next_question(self):
         self.correct_ans.hide()
         if self.generalrbutton.isChecked():
            self.general_knowledge()

         elif self.whrbutton.isChecked():
            self.worlds_history()

         elif self.nhrbutton.isChecked():
            self.nepals_history()

         elif self.sciencerbutton.isChecked():
            self.science_quiz()
    def check_answer(self):
        guess=self.sender()
        if guess.text()==self.ans:
            guess.setStyleSheet("background-color: hsl(134, 61%, 41%);")
            self.correct_ans.hide()
            self.nextquestion.show()
            self.exitcategory.show()
            self.endquiz.show()
            self.score+=1
        else:
            guess.setStyleSheet("background-color:hsl(0, 75%, 55%);")
            self.correct_ans.setText(f"Correct ans : {self.ans}")
            self.correct_ans.show()
            self.nextquestion.show()
            self.exitcategory.show()
            self.endquiz.show()
        self.option1.setEnabled(False)
        self.option2.setEnabled(False)
        self.option3.setEnabled(False)
        self.option4.setEnabled(False)
    def end_quiz(self):
        self.endquizlabel1.show()
        self.endquizlabel2.show()
        self.layout().setAlignment(self.endquizlabel1, Qt.AlignCenter)
        #self.layout().setAlignment(self.endquizlabel2, Qt.AlignCenter)
        self.label1.hide()
        self.label2.hide()
        self.correct_ans.hide()
        self.nextquestion.hide()
        self.exitcategory.hide()
        self.endquiz.hide()
        self.question_label.hide()
        self.option1.hide()
        self.option2.hide()
        self.option3.hide()
        self.option4.hide()
        self.overquestions1.hide()
        self.overquestions2.hide()
        self.endquizlabel1.setText(f"Dear {self.name}, Your score is {self.score}/{len(self.stored_question)}"
                                   f"\nIn percentage: {(self.score/len(self.stored_question)*100):.2f}%"
                                   f"\nHave a nice day!")
    def exit_category(self):
        self.label1.show()
        self.label2.show()
        self.question_label.hide()
        self.option1.hide()
        self.option2.hide()
        self.option3.hide()
        self.option4.hide()
        self.nextquestion.hide()
        self.exitcategory.hide()
        self.endquiz.hide()
        self.correct_ans.hide()
        self.overquestions1.hide()
        self.overquestions2.hide()
        self.generalrbutton.setAutoExclusive(False)
        self.generalrbutton.setChecked(False)
        self.generalrbutton.setAutoExclusive(True)
        self.whrbutton.setAutoExclusive(False)
        self.whrbutton.setChecked(False)
        self.whrbutton.setAutoExclusive(True)
        self.nhrbutton.setAutoExclusive(False)
        self.nhrbutton.setChecked(False)
        self.nhrbutton.setAutoExclusive(True)
        self.sciencerbutton.setAutoExclusive(False)
        self.sciencerbutton.setChecked(False)
        self.sciencerbutton.setAutoExclusive(True)
        self.submit_click()
    def over_questions(self):
        self.question_label.hide()
        self.option1.hide()
        self.option2.hide()
        self.option3.hide()
        self.option4.hide()
        self.nextquestion.hide()
        self.exitcategory.show()
        self.endquiz.show()
        self.correct_ans.hide()
        self.overquestions1.setText("Question Bank Completed!")
        self.overquestions2.setText("You have answered all 5 questions in this category.")
        self.overquestions1.show()
        self.overquestions2.show()
        self.layout().setAlignment(self.overquestions1, Qt.AlignCenter)
        self.layout().setAlignment(self.overquestions2, Qt.AlignCenter)

if __name__=="__main__":
    app=QApplication(sys.argv)
    quiz=Quiz()
    quiz.show()
    sys.exit(app.exec_())