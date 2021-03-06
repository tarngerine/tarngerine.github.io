# ~~When and~~ how to invest in product design tooling
## A guide for thinking about building (or not) a team to improve workflows.

### Why should I listen to you?
I started, grew, lead a team of designers and engineers who revamped the workflow of 600+ designers and thousands of their cross-functional peers. Among other successes, we saved each designer an average of 10+ hours of work a week and used an integrated toolchain to drive design system adoption for Facebook, Messenger, Instagram, Whatsapp, and more.

### What is this going to cover?
I will not cover why it's important to invest in design tooling. I'm assuming you're already convinced that you need to invest in improving your team's own workflow. I'm not going to cover specific things you should build, since every team is unique in their workflows and problems, and there's no way I'll be able to identify broad categories without being overly broad. I'm also not going to cover or compare specific design tools that are on the market, as tools will come and go.

Instead, I want to cover some key things I learned that you may not have thought about yet:

- Resist the urge to build software — look at non-coding methods to improve workflows first
- Show the value you're providing to management to get resources
- Spend time helping your users — that built up intuition from diving deep will make deciding what to build easier
- Startups come and go, carefully consider the likelihood of your company outlasting the latest shiny tool before adopting it
- Form partnerships with key teams across your company to drive adoption
- Identify important company initiatives you can focus your work to support
- There's probably more, but I don't remember!!!

This is a personal recap of sorts of the unique things I learned during my time working on tools. I hope it's helpful!

— Julius

---

# What is design tooling?
> To a hammer, everything looks like a nail. One of the top pitfalls anyone working on tooling will be to think of a tool-based solution for every problem they see.

I want to broaden what's probably in your head when you think about "design tooling". **Design tooling is any tool, resource, or process that a product designer uses to accomplish their goals.** Yes, software like Sketch and Framer are design tools. So are slide decks, emails, task prioritization techniques, and company-specific handoff processes for redlining and specs. So are classes, tutorials, shared resources, and technical support.

Are weekly check-ins adding extra work for your design team to compile process to share with management? Maybe you should automate that. Is the way every designer hands off specs to engineering different and causing engineering churn? Maybe you should standardize that. Is the understanding of data analysis inconsistent across the designers and causing some to be less effective? Maybe you should teach some classes.

Yes, this is an "everything is design [tooling]!" trope, but I think it's important to not be pigeon-holed into what we think design tooling is by what the current industry conversation is. This way, we can achieve our end goal: to improve the workflows of product designers so that they can achieve their goals for the company more efficiently and effectively.

---

### Do I need to code to make design tooling?
No!!! There is a wide array of initiatives and opportunities you can take to improve designer workflow without committing a single line of code. You can define new processes that are more efficient, or host classes and write tutorials on pro-tips with the existing tools you use, create useful shared resources, or even set up a pipeline to outsource repetitive work. You can investigate the latest tooling, and make recommendations on which ones you think the team should adopt, evangelizing and building a community.

---

---

# ***Everything below is draft/WIP***

---

---

### Programs vs Software
A lot of times in resource-constrained teams, the best way to do something is to do it by hand. You don't need to make software for every thing you need. For example, if your team hasn't created proper processes for things...?

A program that's done by hand can eventually become something fully automated

MVP often is still something you built, but consider things that can be done by hand without writing a single line of code.

MVP -> Full featured software
Doing things by hand -> program -> MVP -> full featured software

Before computers, a program was a predetermined structure of activities, often written, that would achieve certain goals.
- Education/training
- Asset/resource pipelines
- Workflows, handoffs, processes
- NEED MORE EXAMPLES!!!

---

## When should I build in-house vs use a 3rd party solution
In software development, there is a coined term called Not-In-House Syndrome (NIH), which is the tendency for teams to want to build something from scratch for more control instead of using a 3rd party solution. In the current state of design tooling, designers swing to the other end of the spectrum, often choosing whatever 3rd party solution is the most popular, likely due to a lack of programming experience and support from their management.

Many design tooling teams start with a hybrid designer and developer, who will have to make a lot of decisions about what to build and more importantly, what *not* to build. There are several important things to balance when deciding what to build, and they vary depending on your company and your team's resources.

### Risks of depending on a 3rd party tool
There is no shortage of 3rd party design tools today. Every month, new startups are funded promising to improve your workflows. Tools that are considered the industry standard can lose favor quickly. Being too deeply invested in a 3rd party tool can lead you to situations out of your control and negatively affect your team's productivity.
- Potential shutdown of tool - in today's sky-high funding for design tools, it's easy to get excited about the latest thing that promises to change everything about your workflow. Keep in mind that a majority of these startups do not last, and that the market for a design tool is limited. Take a look at the company's pricing model and compare that with their investment funding and rate of hiring.
- Not owning your own data - many tools today store your data on their own cloud servers and/or use a proprietary file format. Is what you're storing in there critical to keep around for a long time in a format you can read and convert if needed? A 3rd party tool that just stores snapshots of your work for the week may be inconsequential if lost, but what about all the discussions and decision-making in your primary planning tool? What if the data is leaked?
- Unstable tool development - tools change at a rapid pace, and changes are pushed through auto-updaters without a heads up. Throughout my time working on tools, we have had several breaking issues that corrupted files and shut down productivity for days because 3rd party tools would ship unstable changes or break APIs. This not only wastes your time, but erodes trust in your own tools that you may build on top of the 3rd party tool.

### Cost to develop and maintain a tool yourself
Every tool you build has exponential costs in development, maintenance, user support, and training. It's extremely common for tools to become abandoned and unmaintained without the proper support. Abandonware will end up hurting your team more than it helped, so you need to make sure there is a long term plan for supporting and growing the tool.
- Development time and resources - this is straightforward, but there's the cost to develop and maintain the software, dealing with changes from dependencies (e.g. if you're writing a plugin for Sketch, Sketch's API will change at some point to inadvertently break your plugin, and you'll need to react quickly to avoid blocking your designers)
- Evangelism and training - even if you make an amazing tool, you need to convince your team to adopt it. I've seen many amazing tool out there that did not properly invest in the "non-code" aspects of workflow improvement. Make sure to develop programs for spreading awareness, work with management to push adoption, and allocate time for training and support.
- Managing your managers - without proper support from company leaders, you may not get the engineers or designers you need. You'll need to spend time convincing management to buy in, and set reasonable deadlines to show consistent progress and measured results.

Once you've made the decision to build your 


---

Human-scale

- Education and training [TOP]
- Customer support (your #1 goal) [TOP]
- Programs vs tools [TOP]
- Showing your impact to management (necessary to do your job) [2ND]

Building

- To build or not to build (NIH syndrome) [TOP]
- Deployment and buy-in from the team, investing in your own ecosystem [TOP]
- ~MVP debt~
- ~Outsourcing~

Strategy

- Pairing organizational initiatives with tooling (related to showing your impact to management) [TOP]
- Tooling as a method of control and philosophy enforcement [2ND]
- Managing risk and balancing progress (related to NIH)
- ~How to prioritize cool vs necessary, big bets vs low hanging fruit~
- ~Who to hire~

Areas of unique opportunities for in-house built tooling [2ND]

- Handoff
- Source of truth
- Education and training
- Support
- Enforcing a specific way of working
- Tools for thought, not pictures
- Machine learning and automation

Prerequisites

- This tool or that tool?
- Should designers code?
- Product design's seat at the table
- Capitalism and the quest for efficiency, worker automation