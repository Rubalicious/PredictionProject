function x = getSkewness(I)
    x = (3*(mean2(I) - median2(I))/std2(I));
end