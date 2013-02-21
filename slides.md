# REDCap: Lessons Learned

## Scott Burns

`scott.s.burns@vanderbilt.edu`

This talk can be found at:

- Source: `github.com/sburns/redcap_lessons`)
- Current Version: `ebrl.accre.vanderbilt.edu/static/talks/redcap_lessons`

## Presenter Notes

Notes

---

# Why You're Here

- Your lab has lots of data in various spreadsheets
- Your PI told you to use REDCap
    - (They were probably bugged by VICTR)
- You have databases in REDCap but aren't sure why
- You went to the training but still don't **get** REDCap
    - Don't worry, it's not your fault


## It's hard to **understand** REDCap until you've done it a gazillion times

## Presenter Notes

---

# Why I'm Here

- Lots of data
- Lots of mistakes
- Nobody told us how to do this

## I want to share what we've learned managing many large projects in REDCap

## Presenter Notes

- 4500 records spanning some 13600 columns across 40 redcap projects

---

# When you leave

- What REDCap **is** and **is not**
- REDCap Terminology
- Why you should move any data you care about to REDCap
- A brief taste on some of the *fancier* REDCap features

## Presenter Notes

- Knowing terminology let's you communicate with the REDCap team more
- The more you know what REDCap is capable of, the less you'll try and make it do things it can't
- Convince them that spreadsheets are bad

---

# Web-Based Database

Access from any computing device that has a web browser

Two-dimensional table of `records` (rows) and `field` (columns)

On-the-fly table modifications through a web interface

Concurrent create/read/update/delete actions across users

---

# Safe for PHI Storage

People paid to care about computer security have vetted the application

Spreadsheets of PHI on your laptop == **bad**

---

# Your data lives in the cloud

<img alt="To the cloud" src="http://rack.0.mshcdn.com/media/ZgkyMDEyLzEyLzA0L2YzL2FwcGxlaGFsdHNpLmFZZC5qcGcKcAl0aHVtYgk5NTB4NTM0IwplCWpwZw/7175c0b6/fd5/apple-halts-icloud-push-email-in-germany-due-to-motorola-lawsuit-ffdfcd1232.jpg" height="250">

**Whatever that means**

---

# Your data lives in the cloud

<img alt="To the cloud" src="http://rack.0.mshcdn.com/media/ZgkyMDEyLzEyLzA0L2YzL2FwcGxlaGFsdHNpLmFZZC5qcGcKcAl0aHVtYgk5NTB4NTM0IwplCWpwZw/7175c0b6/fd5/apple-halts-icloud-push-email-in-germany-due-to-motorola-lawsuit-ffdfcd1232.jpg" height="250">

- Professional administration
- Professional backups
- High Availability

---

# Your data lives in the cloud

<img alt="To the cloud" src="http://rack.0.mshcdn.com/media/ZgkyMDEyLzEyLzA0L2YzL2FwcGxlaGFsdHNpLmFZZC5qcGcKcAl0aHVtYgk5NTB4NTM0IwplCWpwZw/7175c0b6/fd5/apple-halts-icloud-push-email-in-germany-due-to-motorola-lawsuit-ffdfcd1232.jpg" height="250">

- Professional administration
- Professional backups
- High Availability

If REDCap goes down and takes your database with it, **you** won't get fired.

