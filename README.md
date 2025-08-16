# crowfunding_## `README.md` Template Phase 1: API Plan

As your Crowdfunding back end grows, you'll have more and more information to put in the `readme.md` file. For now, you have a rough plan for your project, so let's mark it down!

Below is a template you can use to add your plan to your readme. As usual, {{ double brackets }} indicate places where you should insert your own content. So if your name was Sinead O'Connor, you would swap `Hi, my name is {{ your_name_here }}!` to `Hi, my name is Sinead O'Connor!`

If you're looking for a good way to create your Schema diagram in VS Code, check out [the draw.io integration extension for VS Code](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)!

To make editing tables in Markdown easier, you might enjoy [the Markdown All-In-One extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one). With this installed, you can hit tab inside of any "cell" in a table, and the editor will automatically resize all your columns and create a new row if necessary.

```markdown
# Crowdfunding Back End
{{ Klara van den Burg }}

## Planning:
### Concept/Name
{{ The Happy Crab Initiative }}

### Intended Audience/User Stories
{{ Being a hermit crab in modern life isn’t easy.
People think we’re content just living in a bit of sand inside a glass tank—but we dream bigger!

We hermit crabs are seizing this moment to raise funds for the essential supplies we need to thrive. From cozy shells to nutritious snacks, every little bit helps us live our best crabby lives.

So we’re calling on all hermit crab supporters:
Help us build the ultimate crab haven—a place to grow, scuttle, and live happily ever after. }}

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ menu to navigate the site }}
    - {{ log in option }}
    - {{ back to top botton}}
    - {{ crab profiles you can click in to for more information }}
    - {{ links to social media }}
    - {{ money meter how much raised }}
    - {{ money meter how much to go }}
    search page
    search specific fundraiser
display fundraiser
show all inforamtion from fundraiser

- {{ A second page available on the front end }}
    - {{ induvitual crab profiles }}
    - {{ option to pleg money}}
    - {{ money meter how much raised }}
    - {{ what the crab is raising money for }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| /fundraisers | fetch  all the fundraisers |Get | N/A| 200 | non | ---------------------------- |
| /fundraisers| create a new fundraiser      | post   | Json Payload    | 201      | Any logged in user    |
|/fundraisers/1/|
|/pledges/ | Fetch all  the pledges | Get | N/A | 200 | 
|/pledges/ |Creating a new pledge for a fundraiser |Post | Json payload | 201 |Any logged in user 

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
![](./database.drawio.svg)
```backend