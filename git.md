
`git config --global user.name "Sarah Smith"`    
`git config --global user.email "sarah.smith@email.com"`     
`git config --global core.editor "nano"`

`git config --global alias.co commit` - **git co** instead of **git commit**

`git config user.name`    
`git config --list`

/////////////////////////////////////////

`git clone <repository link>`

/////////////////////////////////////////

`git pull origin master`

`git init`

`git add .`

`git commit -m "first commit"`    
`git commit -am "first commit"` - изпраща променените файлове за запис с една команда      
`git commit --amend -m "first commit"` - променя съдържанието на записа      

`git push`      
`git push --set-upstream-to origin new_branch` - създава новият клон в хранилището и добавя файловете      
`git push -u origin new_branch`      

/////////////////////////////////////////

git log - списък с всички запазени версии
git log -n 5 - 5-те най-скорошни записа
git log --since=2019-01-01 - записи направени след датата
git log --until=2019-01-01 - записи направени преди датата
git log --grep "Init" - записи които съдържат init

git help

git status - дава информация за статуса, на кой клон съм и дали има нещо за записване

git diff - показва каква е разликата между файловете в работната папка и тези, които са запазени
git diff --staged - показва каква е разликата между файловете, които са готови за запис
git diff --color-words - показва само променената дума
git diff 12old567..12new567 --color-words - показва само променената дума между тези два записа

git show 12acf567 - показва какво е променено в някой минал запис
git show 12acf567 --color-words

/////////////////////////////////////////

git branch new_branch - създава клон с име new_branch
git checkout new_branch - отива на този клон

git checkout -b new_branch - двете горни команди в едно

git merge new_branch - обединяване на новият клон с основния
git rebase new_branch - копира новият клон в основния

git branch -a - показва всички клони които има проекта
git branch -f master HEAD~3 - преместване на клона три стъпки назад в дървото
git branch -d new_branch - изтрива клона
git branch -m free_branch new_branch - преименуване на клона
git push origin --delete new_test

/////////////////////////////////////////

git checkout --file1.txt - взима файла от последният запис и го променя в работната папка
git checkout 123old23 -- file1.txt - взима файла от този запис и го променя в работната папка

git reset HEAD file1.txt - връща файла от готови за запис до чакащи
git revert HEAD~1

/////////////////////////////////////////

git rm file.txt - изтрива файла file.txt
git mv file.txt new_file.txt - преименуване на файла

git rm -rf --cached . - removes all files from the repository and adds them back (this time respecting the rules in your .gitignore)

/////////////////////////////////////////

git remote -v
git pull upstream master
git checkout -b doc-fixes
git push origin doc-fixes

/////////////////////////////////////////

git commit --amend -m "New commit message." - променя текста на последния запис
git rebase -i HEAD~3 - променя текста на последните три записа като трябва да се сложи reword

git push --force branch-name
