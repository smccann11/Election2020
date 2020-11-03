import praw
import random
import datetime
from textblob import TextBlob

import random
def generate_comment_0():
    adjs = ['good', 'great', 'amazing', 'impactful', 'better']
    adj = random.choice(adjs)
    experts = ['scientists', 'experts', 'social workers', 'smart people', 'people like Fauci']
    expert = random.choice(experts)
    factss = ['facts', 'the truth', 'information', 'real science']
    facts = random.choice(factss)
    aspects = ['certain aspects of life', 'science', 'the unkown', 'some phenomena']
    aspect = random.choice(aspects)
    
    text = "Joe Biden will be a " + adj + " president becasue he will listen to " + expert + " and implement policy based on " + facts + " not feeling. " + expert + " know best, as they have devoted their lives to advancing knowledge of " + aspect + "."
    return text

def generate_comment_1():
    advs = ['fight', 'advocate', 'push', 'champion']
    adv = random.choice(advs)
    adjs = ['kind', 'good', 'sympathetic', 'smart', 'knowledgable']
    adj = random.choice(adjs)
    rights = ['fighting racism', 'income equality', 'the right to an abortion', 'healthcare']
    right = random.choice(rights)
    goods = ['good', 'betterment', 'best', 'future']
    good = random.choice(goods)
    peoples = ['americans', 'the people', 'citizens', 'us']
    people = random.choice(peoples)
    
    text = "Biden and Harris will " + adv + " for the natural human rights of all people. Any " + adj + " candidate would. An example of a natural human right would be " + right + ". Voting for Biden would be voting for the " + good + " of " + people + "."
    return text

def generate_comment_2():
    works = ['work', 'policy', 'ideas', 'achievements']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    fights = ['fought', 'advocated', 'helped', 'improved lives']
    fight = random.choice(fights)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    others = ['americans', 'the people', 'citizens', 'everyone']
    other = random.choice(others)
    
    text = "Joe Biden's " + work + " under the Obama administration " + show + " his passion for the American people. Biden was a major part in revamping the auto industry, and " + fight + " for people. " + person + " vote for Biden is a vote for " + other + "."
    return text

def generate_comment_3():
    works = ['work', 'policy', 'ideas', 'actions']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    fights = ['fought', 'advocated', 'helped', 'improved lives']
    fight = random.choice(fights)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    others = ['profanity', 'hate', 'racism', 'ignorance']
    other = random.choice(others)
    
    text = "Donald Trump's " + work + " under his administration " + show + " his ignorance for the American people. Trump ignored the severity of COVID-19, and never " + fight + " for american people. " + person + " vote for Trump is a vote for " + other + "."
    return text

def generate_comment_4():
    works = ['work', 'policy', 'ideas', 'actions']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    eves = ['evident', 'seen in fact', 'there', 'all throught his actions and words']
    eve = random.choice(eves)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    values = ['values', 'ideas', 'thoughts', 'actions']
    value = random.choice(values)
    
    text = "If you believe the " + work + " of Doanald Trump under his administration " + show + " the best of the American people, re-examine your thoughts. His ignorance for the American people, although maybe not obvious is" + eve + ". Trump ignored the severity of COVID-19. " + person + " vote should align with your best" + value + "."
    return text

def generate_comment_5():
    works = ['words', 'tweets', 'ideas', 'actions']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    eves = ['evident', 'seen', 'obvious', 'shown all throught his actions and words']
    eve = random.choice(eves)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    values = ['health', 'safety', 'equality', 'hope']
    value = random.choice(values)
    
    text = "Trump's " + work + show + "  the person he is. An ignorant, selfish, and stobborn man without sufficient knowledge of skills to be a president. It is " + eve + " that Trump does not care about the average person, but rather himself and his reputaiton. " + person + " vote could end this era, and begin one full of " + value + "."
    return text

def generate_comment():
    for i in range(1):
        options = [0,1,2,3,4,5]
        choice = random.choice(options)
        if choice == 0:
            print(generate_comment_0())
        elif choice == 1:
            print(generate_comment_1())
        elif choice == 2:
            print(generate_comment_2())
        elif choice == 3:
            print(generate_comment_3())
        elif choice == 4:
            print(generate_comment_4())
        elif choice == 5:
            print(generate_comment_5())
generate_comment()

reddit = praw.Reddit('cs40botspen')

reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)

while True:

    print()
    submission.comments.replace_more(limit=1)
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    
    for comment in submission.comments.list():
        all_comments.append(comment)
        
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []

    for comment in submission.comment.list():
        if comment.author=='cs40botspen':
            not_my_comments.append(comment)

    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

     
    for comemnt in all_comments:

        blob = textblob(comment)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        print('comment=',comment)
        print('polarity=',polarity)
        print('subjectivity=',subjectivity)
        print()

    if 'Biden' in comment and polarity > 0: #upvote

    if 'Biden' in comment and polarity < 0: #downvote

    if 'Trump' in comment and polarity > 0: #upvote

    if 'Trump' in comment and polarity > 0: #downvote
    

    
    
