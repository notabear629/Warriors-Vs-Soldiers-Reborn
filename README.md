# Warriors-Vs-Soldiers-Reborn

This bot is NOT the WvS that many of you are used to. It is the work of an absolute schizophrenic and you should not go into this game thinking its the same as the old bot.

It's a different developer, and it's not a 1:1 remake.

# How to run the bot?

First, naturally, you need to clone this repository.

This bot requires Python 3.12 to be ran. So you should have python 3.12 installed, or ran in a virtual environment such as conda. It has some requirements that are listed in requirements.txt, so you can easily get up to speed with a pip install -r requirements.txt

This bot also REQUIRES that MongoDB be installed on your computer. It is recommended just to simply get MongoDB community edition and it is highly recommended to check the "install compass" option in that installer, as MongoDB compass is a great way to manage your database.

You can not run my bot, and I will not be hosting your bot for you. As such, it is required for you to go to discord.com/developers and get your own bot and token.

This bot REQUIRES to be ran in a server specifically built for it, and you need to configure your .env file a certain way.

The ".env.example" file has all the variables pre-arranged. It's just up to you to add values to them. First,

for BOT_TOKEN, you need to paste your token WITH NO SPACES and inside parenthesis, like this.

BOT_TOKEN="yourtokenhere".

BOT_PREFIX should be whatever you want the command starter for your bot to be. For example, if you want ~pick to work, you need to make your .env to be

BOT_PREFIX="~"

DATABASE_NAME_ROOT and DATABASE_NAME_GAME dont matter what you call them, they are just what you want to call the root database and the game specific database that will be visible in compass. You can give these whatever name you want in "". 

The final 5 will take integer arguments and you should NOT use parenthesis to define them.

BOT_HOME_SERVER_ID should be defined as the ID of your server.

BOT_HOME_CHANNEL_ID should be defined as the ID of the channel you want wvs games to be played on.

BOT_USER_CHANNEL_CATEGORY requires some setup. You see, this bot does NOT dm players. It creates personal channels for them to play on. You need to create a channel category for the bot to automatically create channels in. It is important that everyone has "see channel permissions" DISABLED by default. Once you create a category that manages this, you can give this field the ID of that category.

BOT_WVS_GAG_ROLE_ID requires you to create a specific role. I recommend calling it [GAGGED]. You need to configure its permissions so whoever has this role has send message permissions DISABLED in the channel that the wvs game is played in, so gaining this role makes it so the player cannot speak. There is a role in the game that uses this ability.

ADMIN_ROLE_ID requires you to create another role for your server admins to use. you should ONLY give this role to people you want to administrate the server. You should give this role every permission, except admin. Upon using the ~admin command, the bot will toggle the admin privillege of that role on and off. Therefore acting as a switch for the user channels to be visible or not.

**IT IS IMPORTANT THAT YOU GIVE OWNERSHIP OF THE SERVER TO THE ALT. OWNERS CAN ALWAYS SEE ALL CHANNELS, LEAVING PRIVATE CHANNELS IMPOSSIBLE. THEREFORE, DONT PLAY ON THE OWNER ACCOUNT.**

It is also important to create the role hierarchy a certain way. You need to ensure that the role created for your bot is at the HIGHEST, and ensure it has admin privilleges.

Put [GAGGED] the SECOND highest.

Put Admin the THIRD highest.

Once all of these are taken care of, you also will need to invite your bot into my emoji servers if you want to use the default emojis.



