function x = getSkewness(I)
<<<<<<< HEAD
    x = (3*(mean2(I) - median2(I))/std2(I));
=======
    x = (3*(mean2(I) - getMedian(I))/std2(I));
>>>>>>> 6d08dd396a939525c350a844711bac6ee01858b4
end