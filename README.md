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

**IT IS IMPORTANT THAT YOU GIVE OWNERSHIP OF THE SERVER TO AN ALT ACCOUNT. OWNERS CAN ALWAYS SEE ALL CHANNELS, LEAVING PRIVATE CHANNELS IMPOSSIBLE. THEREFORE, DONT PLAY ON THE OWNER ACCOUNT.**

It is also important to create the role hierarchy a certain way. You need to ensure that the role created for your bot is at the HIGHEST, and ensure it has admin privilleges.

Put [GAGGED] the SECOND highest.

Put Admin the THIRD highest.

Once all of these are taken care of, you also will need to invite your bot into my emoji servers if you want to use the default emojis.

The bot is ran by running WvS.py as a python script.

# How to modify the game

One of the key features of the bot is that it is fully customizeable in regards to its theming. In order to add a new theme to the game, you should do some basic steps.

First, in the themeData folder, copy defaultGameTheme and create a new file. Name it something else, and change the class name from defaultGameTheme to something else.

You should use this as a basic blueprint to edit the theming of the game to your heart's content. Just be sure that your bot has access to any custom emojis that you specify.

You also need to make sure that the bot can use your theme by editing Theme.py in the gameObjects folder.

You need to add an import statement to match the other imports at the top of the file for your new class,

and the loadedThemes variable needs to have your new class be added into its list.

You can also change the defaultTheme to change which is the one it starts on from within this file.

# What's new

This game has ***42***! roles, designed after the cast of Attack on Titan by default, including many completely new and original ideas.

This game has a new team that can be played on casual, called Wildcards! Warriors Vs Soldiers... With wildcards? These players are not warriors or soldiers, but have some special objectives they try to achieve.

This game has a SPECIAL alternate ending for games... RUMBLING, RUMBLING, ITS COMING! On casual, its possible for yeagerist factions to start the rumbling, breaking the game from its current state, and re-defining the teams!

DEATH!... Yeah, so its legit possible for you to kill people in this game. Like, cannot be picked anymore, cannot vote anymore, DEAD.

Extreme customization! Not even just with themes, There are so many certain specific combinations of rules you could apply as the host. You can also save many configurations to be loaded at a later time so you dont have to change them all whenever you play. Furthermore... YOU DONT HAVE TO CHANGE THE RULES EVERY SINGLE TIME YOU PLAY! Assuming the bot didn't shut off, it will remember the last rules you played with. So if you want to play with the same rules as the last game, all you have to do is ~host and it's there waiting for you.

Buttons! Theres buttons now. Insane, isnt it?

Webhooks! This is just a little thing i think is cool, but the bot will have little splash messages with a character name and pfp. Is it completely necessary? no. But fuck you i like it and i do what i want.

Unprofessionalism! I just told you fuck you to your face, and my bot can and will do it too.

Sick and tired of disagreeing with your teammate on who to kidnap? NOW YOU DON'T NEED TO. With "Multikidnap", the traditional way of kidnapping is GONE. Now, here is how it works, every single warrior chooses a player to kidnap. If you are a warrior, its simple. If you kidnap right, you win. If you kidnap wrong, you lose. As a soldier, its a bit more tricky. if the MOST POPULAR CHOICE to kidnap is correct... You lose. Otherwise you win. In other words, if there are 3 warriors, and 2 get it right and 1 gets it wrong. You lose. Since the most popular choice was correct. But if 2 warriors kidnap differently and only 1 gets it right, you win, since there was no single most popular choice.

Features for the criminally undecided! Don't want to vote on an expo? now you can refuse and abstain! Don't want to pick an expo? Now you can refuse and ~pass! Have regrets about people you already picked? Now you can undo your TERRIBLE life choices and ~clear to pick the expo again!

10 person limit? HAHAHA. 24 people can join a single game in this bot.

Dynamic expedition sizing! NO more 2 to fail. 5 and 6 player games will remain the same with the traditional expo counts. All other games will use a special form of expedition sizing I call dynamic expos. What happens in this case, is that r1 will always have 2 players. and R2 will always have 3. But, the expedition count of r3 will depend on the results of r2. If r2 passes, r3 will have 4 players. If r2 breaks, r3 will stay at 3 players. The exception for this is if wildcards is enabled and warriors are severely undermanned, where a +1 grace is added for expo counts.

Give up easily? GREAT! Now, as Zeke you can ~retreat in your private channel to immediately go to the basement.

Warrior markers so you can rememeber your teammates/coord info! In the personal embed to what teams you are voting for / are on an expedition, if you are a warrior or a coordinate a little warrior marker will appear next to warrior names, just so you can always remember what you know.

Colored ~status embeds! If soldiers are losing they are red, if winning they're green, if neutral yellow. If lost, black. Makes no difference, but damn it i like it and I do what i want.

INSANE team captains settings. In this bot Coordinate and Warchief are mandatory... OR are they? In casual games, you can edit this so zeke (warchief) is not required... But also that Eren is not required. That's right, you can play a version of the game without a coordinate. Does anybody ever do it? no. Is it even really fun? no. Did I think it would be hilarious to do so did it just to say i did it? Absolutely yes.

Built in custom color management! Tired of people asking you to give them specific hex colors? My bot has a command to give the player any damn color they want, with any hex code of their choosing.

A new leaderboard system, new titles, new badges, and an ABSURD amount of stat tracking! Why? IDK i just like spicing things up and keeping track of WAYYYY too many stats.

More stuff I'm undoubtedly forgetting! Look man, this was a huge undertaking I cant possibly keep track of everything lol







