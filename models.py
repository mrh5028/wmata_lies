from app import db

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    line = db.Column(db.String(64), index = True, unique = False)
    issue_type = db.Column(db.String(64), index = True, unique = False)
    status = db.Column(db.String(64), index = True, unique = False)
    direc = db.Column(db.String(64), index = True, unique = False)
    station = db.Column(db.String(64), index = True, unique = False)
    metro_tweets = db.relationship('Metro_tweet', backref= 'issue', lazy = 'dynamic')
    rider_tweets = db.relationship('Rider_tweet', backref='issue', lazy = 'dynamic')
    
    def __repr__(self):
        return '<Issue %r>' % (self.issue_type)

class Metro_tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tweet_text = db.Column(db.String(128), index = True, unique = False)
    tweet_url = db.Column(db.String(256), index = True, unique = False)
    tweet_time = db.Column(db.DateTime)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))
    
    def __repr__(self):
        return '<Metro %r>' % (self.tweet_text)

class Rider_tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tweet_text = db.Column(db.String(256), index = True, unique = False)
    tweet_url = db.Column(db.String(512), index = True, unique = False)
    tweet_time = db.Column(db.DateTime)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))

    def __repr__(self):
        return '<Rider %r>' % (self.tweet_text)