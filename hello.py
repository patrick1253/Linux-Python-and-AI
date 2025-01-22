def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
		
number = 5
result = factorial (number)
print(f"The factorial of (number) is (result).")

# touch ((filename.ext)) to create a new file
# gedit ((filename.ext)) to edit the file
# git status will give status of local repo
#     - untracked means not tracked by git so far
#     - changes to commit means in git but not committed
#     - nothing to commit means all added files have been committed already
# git add ((filename.ext)) to add the file to git
# git commit -m "message"  (the -m allows you to add a comment, to remember why you made the change.)
# git push origin ((branchname)) to push the changes to github -- must specify the branch you are pushing to (main, unless otherwise specified)
#     - eg: git push origin main
#     - must authenticate:  >github>profile> settings > developmer settings > classic token > generate new classic token
#     - name token, set expiry, select activities > create token
# git remote set-url origin https://<token>/<username>/<repo>


