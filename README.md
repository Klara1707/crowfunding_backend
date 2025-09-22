# crowfunding_## `README.md` Template Phase 1: API Plan

As your Crowdfunding back end grows, you'll have more and more information to put in the `readme.md` file. For now, you have a rough plan for your project, so let's mark it down!

Below is a template you can use to add your plan to your readme. As usual, {{ double brackets }} indicate places where you should insert your own content. So if your name was Sinead O'Connor, you would swap `Hi, my name is {{ your_name_here }}!` to `Hi, my name is Sinead O'Connor!`

If you're looking for a good way to create your Schema diagram in VS Code, check out [the draw.io integration extension for VS Code](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)!

To make editing tables in Markdown easier, you might enjoy [the Markdown All-In-One extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one). With this installed, you can hit tab inside of any "cell" in a table, and the editor will automatically resize all your columns and create a new row if necessary.

# Crowdfunding Back End
{{ Klara van den Burg }}
{{ https://the-happy-crab-initiative-23df300e577e.herokuapp.com/fundraisers/}}

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
    - {{ search page profile}}
    - {{ search fund raiser }}
    - {{ Welcom text }}
    - {{ crab profiles you can click in to for more information }}
    - {{ crab photo }}
    - {{ what the crab is raising money for, one sentance }}
    - {{ pledges under each crab}}
    - {{ pop up window when pledging with thank you}}
    - {{ meter total money raised under each crab}}

- {{ A second page available on the front end }}
    - {{ induvitual crab profiles }}
    - {{ crab photo in profile}}
    - {{ photo of what is being fundraised for}}
    - {{ option to create fundraiser for crab }}
    - {{ option to pleg money}}
    - {{ money meter how much raised }}
    - {{ what the crab is raising money for }}
    - {{ pop up window when pledging with thank you}}
    - {{ pop up window when creating a pledge with thank you}}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL                | HTTP   | Purpose                          | Request Body | Success Response Code | Authentication/Authorisation |
| ------------------ | ------ | -------------------------------- | ------------ | --------------------- | ---------------------------- |
| /fundraisers/      | GET    | Fetch all fundraisers            | N/A          | 200                   | Required (Token)             |
| /fundraisers/      | POST   | Create a new fundraiser          | JSON Payload | 201                   | Required (Token)             |
| /fundraisers/<id>/ | GET    | Fetch a specific fundraiser      | N/A          | 200                   | Required (Token)             |
| /fundraiser/<id>/  | PUT    | Update a fundraiser              | JSON Payload | 200                   | Required (owner only)        |
| /fundraiser/<id>/  | DELETE | Delete a fundraiser              | N/A          | 204                   | Required (owner only)        |
| /user/             | GET    | Fetch all users                  | JSON payload | 200                   | Any logged in user           |
| /user/             | POST   | Create a new user                | JSON payload | 201                   | None                         |
| /user/<id>/        | GET    | Fetch details of a specific user | N/A          | 200                   | Required (Token)             |
| /user/token-auth/  | POST   | Authenticate user and get token  | JSON payload | 200                   | None                         |
| /pledges/          | GET    | Fetch all pledges                | N/A          | 200                   | Required (Token)             |
| /pledges/          | POST   | Create a new pledge              | JSON payload | 201                   | Required (Token)             |
| /pledges/<id>/     | GET    | Fetch a specific pledge          | N/A          | 200                   | Required (Token)             |
| /pledges/<id>/     | PUT    | Update a pledge                  | JSON payload | 200                   | Required (supporter only)    |
| /pledges/<id>/     | DELETE | Delete a pledge                  | N/A          | 204                   | Required (supporter only)    |

### DB Schema
![wireframe_popup]( img\Happ_crab_wireframe_popup.png)
![wirefram_mainpage]( img\Happ_crab_wireframe.png)
![fundraiser_all_fundraisers](img\fundraiser_all_fundraisers.png)
![fundraiser_create_new](img\fundraiser_create_new.png)
![fundraiser_fetch_specific](img\fundraiser_fetch_specific.png)
![user_authenticate_user_get_token](img\user_authenticate_user_get_token.png)

```backend