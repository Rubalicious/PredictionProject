function x = getSkewness(I)
    x = (3*(mean2(I) - getMedian(I))/std2(I));
end