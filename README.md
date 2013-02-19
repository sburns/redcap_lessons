# REDCap: Lessons Learned

This is a talk I'm working on. The gist is that while REDCap can revolutionize your research, it's hard to think about when you're just getting started.

## Generating the presentation

- `$ pip install -r requirements.txt`
- Somehow install `rvm` or `rbenv`
    - `$ gem install sass`

To make the presentation:

`$ fab gen`

To rebuild `screen.css` from `screen.scss`:

`$ fab gen_css`

To rebuild the presentation every little while: (I couldn't get watchdog to work):

`$ fab loop # loop:pause=X`