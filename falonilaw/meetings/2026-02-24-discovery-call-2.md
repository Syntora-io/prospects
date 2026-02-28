# Discovery Call 2 -- Filoni Law

- **Date:** Feb 24, 2026, 12:00 PM ET
- **Attendees:** Parker Gawne, Meghna Shindhe, David Filoni Jr., Sean Barlisan, Darsh Patel, Trisha
- **Duration:** ~37 min

---

## AI Summary

**Programming Resource Needs:** Team requires extra programmers to eliminate bottlenecks in court data processing and ensure 100% uptime.

**Automation Challenges:** Manual input is needed for certain fields, limiting full automation and causing data duplication issues.

**Code Management:** Current codebase is siloed; transitioning to GitHub repositories could enhance collaboration and organization.

**Technical Stack:** Utilizes Python, PowerShell Universal, SQL, and Okta for secure data processing; over a thousand court emails received daily.

**Strategic Next Steps:** Proposal call next Tuesday to review solutions and establish programming support; clear ownership of developed code emphasized.

---

## Key Findings

### New People Identified
- **Trisha** -- Higher-level programming direction (alongside Chris). Concerned about security of any new tooling. Not deeply technical but has authority.
- **Sean Barlisan** -- Confirmed as technical lead for day-to-day scripting. Runs scrapers, manages workspaces, provides code structure to Darsh.
- **Chris** -- Still not on the call. David will try to get him on the proposal call next week.

### Platform Answer: CollectMax (On-Prem), NOT Accis
- They are on JST CollectMax with a production server on-prem.
- No REST API. Everything is file-based (EDI).
- They pull data out of JST into a SQL database for additional processing and reporting beyond what JST can do natively.
- JST has import limitations -- certain fields (e.g. place of employment) cannot be bulk imported because they reference existing dropdown records. Requires click-through automation instead.

### Infrastructure
- **Amazon Workspaces** -- Each programmer gets a designated AWS workspace. Scripts run there or on the JST production server for heavier loads.
- **No centralized repo** -- Code is siloed per workspace. No GitHub, no shared repo. Darsh has some stuff in BitBucket but it's just his scrapers.
- **Python** -- Primary scripting language. Scrapers run hourly (12:01am to 11:59pm daily cycle).
- **PowerShell Universal** -- Used for endpoints, FTP file transfers, report generation, SQL query execution.
- **SQL database** -- Holds data pulled from JST for custom reporting and cross-referencing (e.g. mapping court docket numbers to account numbers).
- **Okta** -- MFA for users (not part of dev stack).

### What the Scripts Actually Do
- **Darsh's 3 scrapers:** Wage confirmation, court officer, goods & chattel. All scan the Jeffers2 email inbox (registered with NJ court system) for specific keywords, extract matching records into Excel sheets.
- **Sean's scrapers:** Similar structure, scan Jeffers3 email (main E-Court contact). Mostly set in stone, don't need changes per Sean.
- **Court filing automation:** Python scripts that click through court website UI (5 clicks per filing). Some may be broken -- "are they still broken?" was asked. Chris owns these.
- **Calendar tool:** Sean building an Outlook calendar tool for the trial team. Nearly done, needs trial team input.
- **FTP downloads:** Extra data string downloads from FTP. Unclear if still needed.

### The Real Job (Trisha's Framing)
- The firm's core operational challenge: **keeping JST as the single source of truth with the most current, accurate data at all times.**
- Data flows IN from: NJ court system emails (1000+/day), data vendors, payment sites.
- Data flows OUT to: Mass court filings (never file one at a time, always in bulk).
- Vendors in India and Africa are on the phone with debtors and need accurate data in real-time.
- Every new programmer's job is contributing to the speed and accuracy of that data pipeline.

### What They Want From Us
1. **More hands writing Python scripts** -- extension of team, not replacement
2. **Unblock Chris and Sean** -- they're bottlenecked, can't get to backlog items
3. **Help with JST import limitations** -- click-through automation for fields that can't be bulk imported
4. **Potentially: GitHub + pipeline setup** -- Sean and Darsh are open to it, researching it already. Team consensus needed.
5. **They own all IP** -- David and Trisha made this very clear multiple times

### What They Don't Need (Yet)
- Existing scrapers are "set in stone" per Sean -- don't touch those
- Chris's filers may need fixing but that's a Chris conversation
- AI is not on the table for this engagement
- Reporting is mostly handled by JST + SQL

### GitHub Discussion
- Parker proposed GitHub repos with branching and Actions pipelines
- Sean and Darsh are open, were already researching it independently
- Trisha's concern: security in their environment
- Cost discussion: Enterprise vs Pro ($20/mo + $8/seat)
- Parker to research licensing options
- Team consensus required before implementing -- "big bridge to cross" per Sean

---

## Action Items

**Parker:**
- Send meeting invite for Tue Mar 3, 12:00 PM ET (proposal call)
- Research GitHub Pro vs Enterprise licensing and cost for their team size
- Develop initial proposal outlining automation solutions

**David:**
- Get Chris on the next call
- Confirm participants for Tuesday

**Meghna:**
- Compile list of repetitive manual tasks beyond current scripts
- Lead proposal discussion next week

**Sean:**
- Provide further technical details on scrapers and calendar tool
- Collaborate with Darsh on GitHub pipeline research
- Serve as technical liaison for new programmers

**Darsh:**
- Document current Python scripts and schedules
- Assist Sean on calendar tool requirements
- Support onboarding complexity estimates

---

## Raw Transcript

Yes.
Awesome. Alrighty.
Just waiting for one more, Sean.
Cool.
Right.
Dar.
Hey, Sean's coming on, right?
Yeah, he's. He's hopping on.
Yeah.
Okay. I do love this. Love the hoodie.
Oh, yeah, it's psg. Hoodie collab with Jordan.
Yeah, dude. No, that collab is sweet. PSG sweet.
That is cool.
Yeah, they've been playing like right now, but like.
Yeah, yeah, they have. Yeah.
You.
You watch the prim at all?
Yeah, I'm a Liverpool fan.
Oh, okay.
They've been doing too, so I can't even say anything.
Well, I'm a Chelsea, dude.
That, that loss of that drone was kind of. Yeah, I thought they were gonna win that game.
I thought so too. Dude. They look good. I don't know. Last minute and it was such a.
Late minute goal too. I was like, nah.
Yeah, yeah, they just were not phased on, dude. Yeah, man. Yeah. What place is Liverpool on this season?
That's a great question.
I think they're like fifth or six now.
Crazy. The final push is going to be nuts. Wow.
Let me. I'll text.
Yeah, I just texted Sean too.
Okay, good.
Awesome. Yeah, well, excited to talk again, guys. It's gonna be a good one today. I think we, me and Magna looked into things pretty heavily on our side. So I guess, yeah, you know, could. Couldn't get in the mock environment of jst. Had to happen with a sales call with someone. But let me get Sean. Cool.
Yeah, he said he'll be right there as he's having microphone issues.
He's on, he's on.
Cool.
There he. Sorry, I was muted. Hello?
Hey.
That's all right.
You're on.
Hey, Sean.
Hello. How are you?
Good, how are you?
I'm great.
I'm great.
Cool.
So, yeah, we wanted to discuss some outside programming. I was, I was telling. Mega. Is that how you say your name?
Yeah,
That's pretty good. Usually I mispronounce everything, but yeah, we need extra programmers to help Sean and Darsh because we have a lot of manual things that we want to make. Sort of like AI and programs. We work on JST software and basically we connect to the courts through our software and we want to make more programs like that so these guys could explain more. Like, you know, the programming side, they're decent at programming but we just, we need sometimes a little help on that. And I think,
Yeah, most of the time we just have so much going on that there's a lot of like bottleneck that we can't really get much done. But like, as Dave Said we mostly work a lot with like the New Jersey court system, the E courts, and a lot of times you also work a lot with jst. I'm sure you've heard of gst and that's mostly like one of the biggest bottlenecks. One of the other programmers, Chris is also helping out with that too, but he also gets bottleneck with other things. But yeah, some more help would also be great.
Bottlenecks. I love it.
That's what it is.
Yeah, it's pretty much we can give more context as to like what we would like, look towards and what we could use more. I feel like that's something that Trisha and Chris would give more context on because Darshan and I, obviously we do see like the high layer things, but I think they could give you more abstract and more deeper ideas of what we want, if that makes sense.
Okay.
But yeah, was there anything else that you were interested in and wanted to know more about what we are looking for?
Yeah, me and Megna, we got some good questions. I think we did some heavy review of jst and I'm familiar, I think that kind of. For this call, we're going to kind of start a little bit of high level and Megda's gonna ask a couple questions and then I'm gonna ask a couple questions. And if we could just hear your guys's input, that would be great because that would kind of point us in the right direction. Okay, cool.
All right.
I do have Trish in here.
Cool.
So where'd I leave off?
Oh, it was about some of the.
Stuff that we could get help with.
Okay.
Yeah, Like Trish was just explaining one thing. This is just, we're not doing anything. These are things that we could use.
So, you know, whenever possible we try to. We try to do everything in a mass at one time. Of course, we try to use recording and Excel whenever possible, but sometimes it goes beyond that. You know, it takes somebody opening a document, copying information and putting it someplace else. You know, so we can't do that just within Excel or, you know, there's limitations sometimes to our program of what they'll let us import. So now we're having to one by one go in and populate this information. So which is fine except for when we have a thousand, two thousand of them, then that's not fine. Then we start talk, you know, going into how long it would take a human to do that. And now it seems beneficial to pay for the initial programming and, you know,
Keep it working, keep working 100%. So one thing we, we had, you know what it is I guess it's run on Python and it clicks through the websites and you have like five clicks that you have to hit.
Yes, well that's, you know, that's importing stuff into our system, our, you know, our data jst, which holds our data. We're able to import a lot of things, but not everything. And there's, we also use, you know, there's times where we have to enter things into the court site. So we used to use some program. We do have Python scripts that do that for us. We could use more because that's everything we do really is, you know, either taking data from the court and putting it in our system or the opposite, taking it from our system and putting it in the court.
So,
You know, anything that could help us do that is beneficial.
Okay, yeah. My first question would be could you just elaborate more on what kind of data you are currently having trouble importing versus what is working?
So sometimes, usually if it's just a blank field, we're able to import data. But sometimes in the program you can't just import in that field. It has to be. One example is, you know, we have people's place of employment and that is saved already in the program. So we can't go putting it again because it already is attached to that person. So then on the back end we'd have, you know, millions of employers if every time we wanted to put it on another screen we had to enter another employer. So what we have to do is say we have to like click the drop down menu and choose the one that is already there. Because sometimes they have two employment, two places of employment. So we have to choose the one that we want and then it populates the screen.
So that's just an example of something we're having an issue with at the moment that we can't just go and auto populate because it's already in the system. We can't just on the back end have a zillion employers. So that's just a little example there. Trying to think of another example.
And Sean, when were going over the calendar stuff, I think there was some things that they wanted to do on that.
Oh, for the outlook wonder. Right. Like the trial team.
I don't know if we ever got to that.
It's actually nearly done. I just kind of needed to talk to like the trial team to see what else they needed.
Okay, cool.
Yeah, that's all I really needed from Them.
And how about, like, downloading the. The downloading things from the FTP, like that extra data string? We want to. I don't know if that's needed or anything either, but I guess we need to get a list together of things that we really want. So. But that's.
That.
That's basically what we're doing. And. Yeah, I mean, I don't know if you guys could help us with that and what the price would be, but.
Yeah, no, yeah, thank you so much for outlining that. That's kind of something similar that I just kind of created a similar Python script for backfilling. But I think that to break this down further for. To just kind of break it down, I would like to start at the very beginning for some of these things. And I know that Magna had a couple of questions, so I would like to hand this over to Magna so she can ask her questions and then I will ask mine.
Yeah, so if you think about where your. Where your staff spends the most amount of time on manual, repetitive tasks, what comes to your mind first? If you could elaborate on that.
So repetitive tasks, what comes to mind first?
Yeah,
We would not. We would rather not have people doing that. You know, if it's a repetitive task, we want it to be done in a program. Is that what you mean? Is that.
I think she means, like, what examples, like all, like the paralegals, like Lindsay or Jessica or like Caroline. Like, what are, like, some of the tasks like, that they're doing, like, that could be automated so they don't have to do it in like, like manually, like themselves. But I don't know what they specifically do. Like, repetitive. Repetitively.
Oh, them? Yeah, no, we don't really. They don't really do that much because we have programs that go. And I don't know, are. The Pythons, are they still broken or should we try to fix them, make them better?
I don't know.
Are they working?
I feel like that's more of a Chris question. These are like the filers, correct? Yeah, yeah, I haven't really touched much on those. Darsh. Would you have any information on that?
I don't touch any, any of that kind of stuff, dude.
Yeah, the ones that create. I wouldn't mess with the ones that are created, right?
Yeah.
If we want to create new ones.
Yeah.
Then I'd say then that's fine.
Right. Okay.
But we can demonstrate how somehow it works and everything like that, and we could come up with other things that we need.
Yeah. So these Python scripts that you're talking about, what do they do exactly? Like what do they solve?
Darsh. Do you have any, can you give context on that?
Because I'm not sure some of the Python scripts, right? So like, at least for me, I have three of them that I use. I have a wage confirmation one that I have a court officer scraper and then goods and channel. So basically like my Python scripts, they just run through a certain inbox in a Jeffers 2 email that we had that's registered with like the NJ court system. And when I'm looking for like when I'm running like my wages, when I'm filing wages, me and trader run wages, right? Whatever goes through that inbox that has like the certain like keyword wage application. Like that's what my like script looks for. Like certain like that keyword. And then I like when I get like a Excel sheet based off of that like that code, right?
I can like look at like my wages and see like, okay, like I got 500 like on my code and it matches with like 500 on like, like on my wages. Like that I filed on like the court because we get a log of that too, right? So that's pretty much like my like what my wage confirmation core officer scrape and my goods and child does like wage confirmation looks for that wage confirmation. The court officer looks for like the certain court officer and what court they're going to, what the case is. The docket number of from JST obviously like connected from our database and then my goods and channel one. It's exactly like the wage confirmation one. It's just two separate like words that we look for. So those are the three scripts that I run.
Sean has a couple of scripts that he also runs that I'm sure that he can explain better because I, I really haven't looked into his codes that much. But yeah, that I've ran basically based like the structure of the code Sean's been providing for me, so he had a better sense of that.
But yeah, for relation to my programs, they're mostly just scrapers for the jeffers3 email, which is the main contact for all the E Court stuff. But majority of it, I feel like that doesn't really need to be touched upon because I feel like that's already just set in stone and nothing needs to be changed.
I feel like that's all that there.
Is for that end though. I'm not sure what else I can,
I'm sure we can come up with some. Some tasks. But I guess there's a few things I wanted to know. Would it be like a. A set price, an hourly price? Are the programs hours? Is there a fee to maintain them? And like, time frame, let's say, for coming up with a intermediate Python program.
Yeah.
That those are all really great questions as far as providing those programs. I think that we really need to understand the general scope of things before we can give a specific price. My whole angle with this is that you would definitely own all of the ip. Everything that would be completely controlled and owned by you. But we can come in as needed if you guys need for kind of a retainer. But that can all be disclosed. My question is, where are these Python scripts currently running? Are they being running pycharm, a different ide, or just straight through? Does JST allow us to just import scripts directly?
So the scrapers run off of these Amazon workspaces? I'm sure you've heard of those. And for certain things with jst, it runs directly on the JST production server.
Awesome.
Yeah, we have one other programmer and we designate an Amazon workspace for them, and anything that they run just runs on that whenever it's set. Some things that are a bigger load would probably run right on production server.
Awesome. Is everybody's code siloed out and collectively uploaded to a central GitHub that stores all of the code in combination with all that stuff? Is that something that's in place?
No, we designate the workspaces, like, so you would have your own designated workspace to run your code.
Okay. And would you guys be opposed to kind of. Kind of having a. Almost a workspace in GitHub alongside your current setup to kind of consolidate things and just silo things out and have different branches?
Not opposed to that? No.
Okay. Yeah.
We just want to make sure we.
We own.
Sorry, what are you saying, dude?
I just said. Yeah, what he said before is we own the code, so.
If we break it, we own it. Just kidding.
And Darcy was saying,
Yeah, I could chime in on that. So I wanted to try to sort of implement that as like a future thing for the. For, like, felony log group. But I haven't yet really, like, dove into it more with, like, the team.
Yeah.
But it was just something that I was researching on my own end alongside with Darsh. But yeah, That's kind of. That's mostly just it. Like we're. That's just something that we're kind of just diving into. But we. I don't see any reason to oppose It.
Okay. The reason that I say that is that for many clients I've uploaded and kind of controlled a lot of things from GitHub and worked alongside of AWS servers and that session building APIs there. However, I believe that if we leverage GitHub Actions and created automation pipelines for these pipelines, Python scripts, it would just kind of bring everything together and we can kind of, I don't know, organize it maybe that way. It's just a thought, but I'm curious to see what you guys think about that.
I. Trisha, do you want to chime in on this or should I?
You know what? I really don't know enough to chime in on it.
I can give context if you'd like.
Yeah, yeah. The only, I mean, of course, Sean, the only thing I am worried about is if, you know, we can secure it in our environment, but I'm sure we can if everyone else is using it. So, I mean, then I'm open to it.
Yes.
Yeah. For the pipelines option, I. Well, I have a lot of experience with it and I would say it's not too hard to really dive into it, especially if were to go somewhere towards like, obviously like using Jenkins or using GitHub Actions. But I, I want to say that obviously it's not my decision, obviously it's something that like the whole team should really go over because it's a big bridge to like cross. But I think most of the processes would be great to work with for the pipelines. But obviously that's something I still want to go over and the whole team should go over first.
Okay.
Yeah. And I, I was just bringing that as a thought because from an outside perspective I, I wanted to bring everybody together and I wanted to kind of decrease the gap between like who has what scripts and which that, I feel like that would be something that if we could help implement off the get go, it could help kind of structure things on for also another programmer to come on and you know, he would have his own separate branch. He would have ownership of a specific silo of a, a repository or I guess a code base full of scripts. And then we could leverage the pipeline there and then obviously it would work alongside your existing setup too.
Okay.
Yeah.
I also had a small question.
Yeah.
So with. If were to go towards using GitHub as obviously the pipelines and the code repo, obviously that's something that still requires monetary expenses. Right. Because you would have to pay for.
The Enterprise Edition yes, that is so true. And the Enterprise edition, from my standpoint, it's not bad, but also it just depends on how many users we need. We could really just get by using the pro version and just adding seats. And the Pro version is $20 a month plus $8 a seat. It is scalable. I don't believe that we necessarily absolutely need the Enterprise version, but I can be wrong and I can look into that in my end.
That'd be great. Okay.
Yeah. So as far as JST goes, so when you guys are getting all your information, you're building scrapers to search for specific keywords that come from an email. Like Darsh was saying, with the wages that is triggered scraper, like, is it run on, like, a specific schedule or are you, like, manually pressing run script?
I have that running every day of every hour.
Okay, cool. So it's. Okay, so it's on a. It's not a timed thing. Awesome.
Same thing with the cord scraper and the goods. Yeah.
Cool. So it's every hour and then. Is it every hour? Like, and then it stops after the working day is done.
Yeah. So, like, at 11:59pm like, it'll stop and then at like 12:01, it'll restart again, the process.
Cool, cool. Okay. All right. I got a lot of my questions out of the way. I know Magna has another question or two. Yes.
Yeah. So do you guys produce reports for your clients? And how do you do that? Like, is that manual or. Yeah, just. Just walk me through that reporting process.
We do it through an FTP site, reporting to our clients. I shouldn't say anything.
Yeah, no, we do. Reporting is done through, you know, from our.
JST software.
Yes. So that's our. That's where it collects all our data. So that's where the reporting comes from. Other than that, we don't really do any.
Yeah, and it goes through the download process.
Okay, so it produces the reports on its own. The GSC software. Yes. So, and then it comes with some preset reports and then some that we can just create on any field that is, say, pullable in the software. But we did kind of. I think we do pull some data and put it into a SQL database that we use for some of the other programs. Because we do have this issue, but I think we've solved it. Right, Sean? That we. Because we pull the county docket, which gives us the account number.
Yeah, that was resolved.
Okay. So that. That currently works. So, you know, the. Like I said, the program has limitations. So I know that to Solve some of those limitations. We could just pull all the data out and then, you know, we can use it the way we wish instead of limited to whatever the program can do. So that's one of the examples.
That.
We use it for is, you know, our unique value is our account number and the court gives us a docket number which is not a unique value, but if we pair it with the county, then it's unique and equals our account number. So now, you know, that's how we're able to take an email. So they send us emails with a docket number now, not an account number. So it really isn't usable to us unless we have an account number for reporting or importing. So that's just an example of how we currently use it. I don't know if you would want to use our current setup that pulls the data into the SQL database just so we have it at will for any of the future programs to be spun off of that data, you know. Okay. Okay.
Also, so do you have like a consolidation of all the, maybe your company data and like if someone new comes to your company, how do they like merge in and. Yeah. How long does it take for them to understand everything? There is quite a learning curve, but I don't know. Darsh. How long did it take you to understand you're still learning? Honestly.
So I, I started in like September, right. And I just started working full time like end of January. So from like the three months I started full time. I would say it's like pretty, it's pretty easy transition. It's not so much like what you're given, it's just like, okay, like if you're giving this, can you like do it within like this time frame and then like, you know, actually do it accurately, like.
Yeah.
Can you put your best foot forward? I think like, you know, it's not that much of like a transition. It's just how you take in mentality, I guess. But it's just, I feel like the, what do you, when you, like when you're new, the learning curve is just, it's not that big. I, I, I would feel like it's just like if you're coming out of college, I feel like it's easy because you're already from like that mindset. Like you're going from a, from learning new information to processing that information now. So for me that gap wasn't too big. But if you're like someone that's not coming from school and you're going into like this type of work, there is going to be like, you know, a type of learning curve.
Like, you're gonna have to, like, read more documents and, like, understand what, like, it's actually saying than, like, you know, just assuming like, the first two lines and just like, you know, going based off of that. But. And from a coding perspective, it was much easy because I have Sean.
Sean.
Sean gives me, like, the proper structure of code and explains like, the proper stuff. So it's just easy to, like, learn from there.
That's awesome.
So I think what makes it difficult is that we're a law firm, right? But really, when you get down to it, I mean, it's not that we're filing things with the court. We're always trying to file as many as we can, but of course, accurately. And the only way we can do that accurately is to have all the information in our database to be the most current and true information all the time. So if, you know, we get sometimes over a thousand emails from the court in a day. So how are we going to update our system so that when we go to file something tomorrow, we have the most true and accurate information that's up to date. So. And it's not only from the court there, it's from other avenues, too.
We have data vendors where we pay for data and then we have to put that data in. And of course, our payments site, you know, those have to always be accurate so that when we're charging somebody a balance, it's the most accurate upstate balance. So we have all these avenues that are sending us data, and we're always having to put it into our one database to make sure that's the most accurate all the time. So. And then, of course, we try to get it out of the database so that we can file everything. We never file one at a time. We file in a mass. And just how. How we. How we have to do it in this type of law.
So I think if we have that mindset that it has to be, you know, our database has to be the most true and accurate all the time. We have vendors india and Africa and they're talking to people on the phone and we want to make sure they're giving them true and accurate information. So I, you know, if I think that's our one job is to make sure that we collect all the data that's coming in from us and put it into the system as fast as possible then and as accurate as possible, then we're doing our job.
Thank you so much for Outlining that they gave a lot of clarity as far as what the expected new programmer would come in and contribute towards. So just to reaffirm that is kind of what you guys would be looking for as far as someone new coming in is someone that is going to be contributing to that speed, but accuracy of those of the database and just of the information in general through Python scripts and just. Of course, yeah, okay.
Yes. And of course Sean and Darsh helping to make sure that everyone is up and running and able to do their job and the programs are up and running and then to be the link to you if it's something that they can't handle on their own.
100%.
Okay.
Oh, sorry. My question completely left my brain and now it is. If we can just get clarity, I know that we've kind of gone over a lot of the tech stack. Can I just get a full clarity on the entire tech stack that's involved in running these Python scripts? So we already know it's jst, we already know that it's AWS servers. We know that you guys could potentially decide to kind of shift towards GitHub, if that makes sense. But Sean or Darsh, do you guys have any other things that you guys have been using?
Yeah, Darsh, let me know if I missed something. I know I'm guaranteed to at least miss one thing. But some stuff that we do use is we obviously also incorporate some PowerShell universal. That's also where a lot of the endpoints exist. If were to perform things like send the FTP or send files through the FTP to one of our clients, generating reports, gathering the SQL information or gathering information from a query to our SQL database. I'm pretty sure you mentioned before, obviously we use the SQL database as well. I believe one other thing that we do use actually it's not really part of it. Yeah, no, but I feel like that really just covers all of it.
It's mostly just the Python using the workspaces to connect through to other stuff JST and as well as like everyone else in the team SQL to hold the main information PowerShell Universal for endpoint and other data. I'm not sure if I really want to count Okta, but that's another MFA and other stuff that we use for a lot of the users. But. But that's not really part of the big development plan that we have in terms of like programming and other things.
Yeah, well, thank you for outlining that. Dark Studio. Do you have anything to add there?
I don't know If Sean wants to add it.
But we've.
I don't like, you know, that BitBucket thing.
Oh, no. Well, yeah, that was one of the things I was looking into when I was mentioning the GitHub repo like earlier. Like, that was a side project I was looking into, but I wouldn't really count that so far. That really only holds like my scraper code and that's kind of just that cool.
Well, yeah, no, thank you for online. That gave me a number of clarity. Man, I love powershell. That's all I do every day is I'm just literally in the terminal. It's literally my entire day. Yeah. Well, thank you guys so much for your time today. We've gotten a of lot of good information. Magna, do you have any final kind of questions as we wrap this up?
No, no. You look kind to them.
Okay. Yeah. So I think next steps would be is we're going to take this and we're going to kind of come to a final kind of proposal phase where we're going to outline solution. You know, it's there. As we continue to move together, I think that there's always going to be discovery. You know, we're going to constantly be asking questions and that's just something that we're going to, you know, just be learning as we go. But yeah, I think. Would it make sense to have a kind of final kind of proposal call next week? Sure, yeah. Okay. Is there a specific date that works best than others?
Mondays are usually terrible.
Fair.
Tuesdays actually work for me are good.
Okay.
And these guys are always around, so.
Yeah. Okay.
Would Tuesday around the same time work? Sure, yeah. Tuesday at 12? Yeah. Okay, well, I guess this 12 my time. Yeah. Okay, well, I will send out that invite and yeah, I'm so grateful for the call. Thank you guys all for, you know, chiming in. And I'm really looking forward to potentially working together.
Yeah, definitely. We'll try to get Chris on too.
Yeah, yeah, that'd be cool. Yeah. Just let me know if you want to add anybody else to the call. I can add them, but until then, I hope you guys have a great rest of your week and good weekend and then we'll pick it up next week. Thank you.
Thank you. Nice to meet you.
Nice to meet you. Thank you.
Nice to meet you. Bye, guys.
Bye.
Bye.
