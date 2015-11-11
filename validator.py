__author__ = 'Naleen'

import pickle

import numpy as np
import cv2
import Orange





# from scipy. skimage import img_as_ubyte
from src.mapper import feature_mapper
from src.scripts import normalize, fileIO, locate_character, prob_match
from src.mapper import validate_mapper
import time
from src.scripts import loadfile


np.set_printoptions(threshold='nan')




def validator_char(start, end):
    # lowerZoneLabels, middleZoneLabels, upperZoneLabels, classifier_middle, classifier_lower, classifier_upper=loadfile()
    img = cv2.imread('C:/Users/Naleen/PycharmProjects/CharReco2/data/chars - Copy.jpg')
    iMax = 109
    jMax = 41
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    dataString_middle=""
    dataString_lower=""
    dataString_upper=""
    char_matrix = {}
    lowerZoneLabels = fileIO.read_label_file('learner/lowerZoneLabels')
    middleZoneLabels = fileIO.read_label_file('learner/middleZoneLabels')
    upperZoneLabels = fileIO.read_label_file('learner/upperZoneLabels')
    classifier_middle = pickle.load(open('learner/ANN_middle'))
    classifier_lower = pickle.load(open('learner/ANN_lower'))
    classifier_upper = pickle.load(open('learner/ANN_upper'))


    for j in range (start, end):
        for i in range (1, iMax):
            time_start=time.time()
            character = gray[64*(j-1):64*j, 128*(i-1):128*i]
            character = normalize.get_mask(character, 5)
            xMin, xMax, yMin, yMax= locate_character.char_location(character)
            # cv2.imshow("sd",character)
            # cv2.waitKey(0)





            dataArray_middle = feature_mapper.middle(character, 21, 43, xMin, xMax)
            dataArray_middle.append('m1')
            # print dataArray_middle

            dataArray_lower = feature_mapper.lower(character, 42, 64, xMin, xMax)
            dataArray_lower.append('l0')

            dataArray_upper = feature_mapper.upper(character, 0, 22, xMin, xMax)
            dataArray_upper.append('u0')


            # MiddleZoneClasss = classifier_middle(dataArray_middle, Orange.classification.Classifier.GetBoth)
            MiddleZoneProb = classifier_middle(dataArray_middle, Orange.classification.Classifier.GetProbabilities)
            UpperZoneProb = classifier_upper(dataArray_upper, Orange.classification.Classifier.GetProbabilities)
            LowerZoneProb = classifier_lower(dataArray_lower, Orange.classification.Classifier.GetProbabilities)

            MiddleZoneClass=(classifier_middle(dataArray_middle, Orange.classification.Classifier.GetBoth))
            UpperZoneClass=(classifier_upper(dataArray_upper, Orange.classification.Classifier.GetBoth))
            LowerZoneClass=(classifier_lower(dataArray_lower, Orange.classification.Classifier.GetBoth))
            # print MiddleZoneClass
            # char1=char_mapper.char_map(LowerZoneClass, MiddleZoneClass, UpperZoneClass)
            # print char1
            print str(i)+ "####################"

            predicted_char, lower, middle, upper = prob_match.probability_match(lower=[LowerZoneProb,lowerZoneLabels],
                                                middle=[MiddleZoneProb, middleZoneLabels],
                                                upper=[UpperZoneProb,upperZoneLabels])

            # char_mapper.char_map()
            input_char= validate_mapper.char_map(i)
            time_end=time.time()
            print str(input_char)+" : "+predicted_char+"   "+lower+"  "+middle+"  "+upper+"     time:"+str(time_end-time_start)

            # char_matrix[input_char]=predicted_char

            char_matrix.setdefault(input_char, []).append(predicted_char)


    for key,values in char_matrix.items():
        predicted=""
        m=0
        k=0
        for value in values:
           k=k+1
           if(key == value ):
               m=m+1
           predicted=predicted+", "+value
        # print k
        # print m
        print str(key)+" : "+str(m/float(k))+" : "+str(predicted)






# validator_char(zone='upper', start=30, end=41)
validator_char(start=30, end=40)



