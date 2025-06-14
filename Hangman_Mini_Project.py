import tkinter as tk
import random as r

words=['python','java','hangman','computer','programming','developer','artificial','intelligence','database','science','algorithm']

def pick():
    return r.choice(words)

def show(w,guessed):
    display = []
    for l in w:
        if l in guessed:
            display.append(l)
        else:
            display.append('_')
    return ' '.join(display)

def start():

    #getDisplay
    #checkGuess
    #updateGame
  
    word=pick()
    guessed=[]
    a=5
    
    root=tk.Tk()
    root.title('Hangman Game')
    root.geometry('500x500')  

    def getDisplay(w,guessed):
        return show(w,guessed)

    
    wordLbl=tk.Label(root,text=getDisplay(word,guessed),font=('Times New Roman',16))
    wordLbl.pack(pady=20)

    attemptLbl=tk.Label(root,text=f'Attempts left: {a}',font=('Times New Roman',14))
    attemptLbl.pack(pady=10)

    guessEntry=tk.Entry(root,font=('Times New Roman',14),width=5)
    guessEntry.pack(pady=10)

    statusLbl=tk.Label(root,text='Good Luck!',font=('Times New Roman',12))
    statusLbl.pack(pady=10)


    def checkGuess():
        nonlocal a
        guess=guessEntry.get().lower()

        if len(guess)!=1 or not guess.isalpha():
            statusLbl.config(text='Please enter a valid single letter.')
            return

        if guess in guessed:
            statusLbl.config(text="You've already guessed that letter.")
            return

        guessed.append(guess)

        if guess in word:
            statusLbl.config(text=f'Good guess! {guess} is in the word.')
        else:
            a-=1
            statusLbl.config(text=f'Sorry, {guess} is not in the word.')
        
        updateGame(word,guessed,a)

    def updateGame(word,guessed,a):
        
        wordLbl.config(text=getDisplay(word,guessed))
        attemptLbl.config(text=f'Attempts left: {a}')

        if a==0:
            statusLbl.config(text=f'Game Over! The word was: {word}')
            guessEntry.config(state='disabled')
    

        elif all(l in guessed for l in word):
            statusLbl.config(text=f'Congratulations! You\'ve guessed the word: {word}')
            guessEntry.config(state='disabled')
    
    
    guessBtn=tk.Button(root,text='Guess',font=('Times New Roman',14),command=checkGuess)
    guessBtn.pack(pady=10)
    
    root.mainloop()
    
start()