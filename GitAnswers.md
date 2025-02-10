1) Git is a distributed version control system, while GitLab is a platform built on Git that provides tools for code management, CI/CD, and team collaboration, a sort of online server.

2) GitLab, GitHub, and Bitbucket are all Git repository hosting services. GitLab is open-source and offers built-in CI/CD, GitHub is the most popular for open-source projects with strong community support, and Bitbucket is often used by enterprises, especially for private repositories and integration with Atlassian tools.

3) You might use Git without GitLab if you only need local version control, want to self-host repositories without a Platform.

4) git add <file name>
git commit -m "description of the changes"
git push

5) A branch in Git is a separate line of development that allows you to work on new features or fixes without affecting the main codebase. It helps in parallel development, testing, and collaboration before merging changes into the main branch.

6) You can see the structure using: 

git log --graph --oneline --all

and it will be something like this: 

o--o--o main branch
   |
   o new branch

7) not really sure what to do

8) Yes, Git is suitable for LaTeX documents because it tracks changes efficiently, enables collaboration, and allows version control. However, for .pdf files, it's better to track only the .tex source files because .pdf is a binary type.

9) Versioning Word and PowerPoint files in Git is not ideal because they are binary files, making diffs and merges difficult. Instead, consider using Google Docs/Slides for collaboration or LaTeX for better version control.

10) If you push your latest commit without pulling first, you could encounter conflicts if there are changes on the remote repository that you don't have locally. This can result in your push being rejected until you resolve the conflicts by pulling, merging, and then pushing again.

11) When you pull without committing your local changes first, Git will attempt to merge your uncommitted changes with the changes from the remote repository. If there are conflicts between your local changes and the pulled changes, Git will prevent the merge and prompt you to resolve the conflicts before proceeding.

12) Branching creates a separate line of development within the same repository, allowing you to work on different features or fixes. Forking creates a copy of a repository under your own account, allowing you to make changes independently and propose them back to the original repository via a pull request.