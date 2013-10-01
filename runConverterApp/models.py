from django.db import models

class runConverter (models.Model):
    milesPerKm = models.FloatField(default=0.621371)
    minMiles = models.FloatField(default=0)
    minKm = models.FloatField(default=0)
    mph = models.FloatField(default=0)
    kph = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):  
        """can't work out how to check most recently changed field, so checking all"""
        if not self.minMiles == 0:
            self.gotMinMiles(self.minMiles)
        
        if not self.minKm == 0:
            self.gotMinKm(self.minKm)
        
        if not self.mph == 0:
            self.gotMph (self.mph)
         
        if not self.kph == 0:
            self.gotKph (self.kph)
    
        super(runConverter, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return (str(round(self.minMiles,2)) + " minute miles is " 
        + str(round(self.minKm,2)) + " minute kilometers is "     
        + str(round(self.mph,2)) + " mph is "     
        + str(round(self.kph,2)) + " kph.")
    
    milesPerKm = 0.621371
    
    def gotMinMiles (self, mm):
        self.minMiles = mm
        self.minKm = mm * self.milesPerKm
        self.mph = (1/float(mm)) * 60
        self.kph = (self.mph)/self.milesPerKm

    def gotMinKm (self, mkm):
        self.minMiles = mkm/self.milesPerKm
        self.minKm = mkm
        self.kph = (1/float(mkm))*60
        self.mph = self.kph*self.milesPerKm

    def gotMph (self, mphIn):
        self.minMiles = 1/(float(mphIn)/60)
        self.minKm = self.minMiles * self.milesPerKm
        self.mph = mphIn
        self.kph = mphIn / self.milesPerKm

    def gotKph (self, kphIn):
        self.minKm = 1/(float(kphIn)/60)
        self.minMiles = self.minKm / self.milesPerKm
        self.kph = kphIn
        self.mph = kphIn * self.milesPerKm

    def getMinMiles (self):
        return self.minMiles
    
    def getMinKm (self):
        return self.minKm

    def getMph (self):
        return self.mph

    def getKph (self):
        return self.kph





# Create your models here.

class tester ():
    r = runConverter()
    r.gotMinMiles(10)
    print "if min miles is 10"
    print "min miles is"
    print r.getMinMiles()
    print "min km is"
    print r.getMinKm()
    print "mph is"
    print r.getMph()
    print "kph is"
    print r.getKph()
 
    r.gotMinKm(6)
    print "\n\nif min km is 6"
    print "min miles is"
    print r.getMinMiles()
    print "min km is"
    print r.getMinKm()
    print "mph is"
    print r.getMph()
    print "kph is"
    print r.getKph()
    
    r.gotMph(6)
    print "\n\nif mph is 6"
    print "min miles is"
    print r.getMinMiles()
    print "min km is"
    print r.getMinKm()
    print "mph is"
    print r.getMph()
    print "kph is"
    print r.getKph()
    
        
    r.gotKph(9)
    print "\n\nif kph is 9"
    print "min miles is"
    print r.getMinMiles()
    print "min km is"
    print r.getMinKm()
    print "mph is"
    print r.getMph()
    print "kph is"
    print r.getKph()