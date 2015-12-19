function table = getStats( files, index, table )
% return all the stats we want fir a photo and populate a table to 
% create an n-dimensional space
% pass in photo name, index, and table being modified



for file = files'
    rgb = imread(file.name);
    % averages and standard deviations
    average = mean2(file.name);
    stdev = std2(file.name);
    range = max(file.name)-min(file.name);
    gray = rgb2gray(rgb);
    avggray = mean2(gray);
    % modes
    graymode = mode(mode(gray));
    rmode = mode(mode(rgb(:,:,1)));
    gmode = mode(mode(rgb(:,:,2)));
    bmode = mode(mode(rgb(:,:,3)));
    % quantiles
    fvec = quantile(rgb,0.25);
    fquantile = squeeze(quantile(fvec,0.25));
    svec = quantile(rgb,0.5);
    squantile = squeeze(quantile(fvec,0.5));
    tvec = quantile(rgb,0.75);
    tquantile = squeeze(quantile(fvec,0.75));
    % kurtosis and skewness
    k = getKurtosis(rgb);
    s = getSkewness(rgb);


    %populating table
    table(index,1) = index;                     % ID
    table(index,2) = average;               % average color
    table(index,3) = stdev;                 % standard deviation
    table(index,4) = range;                 % range
    table(index,5) = min(file.name);        % minimum value
    table(index,6) = max(file.name);        % maximum value
    table(index,7) = avggray;               % average grayness
    table(index,8) = graymode;              % most common gray color
    table(index,9) = rmode;                 % most common red color
    table(index,10) = gmode;                % most common green color
    table(index,11) = bmode;                % most common blue color
    table(index,12) = fquantile(1);         % first quantile
    table(index,13) = squantile(1);         % second quantile (median)
    table(index,14) = tquantile(1);         % third quantile
    table(index,15) = k;                    % kurtosis
    table(index,16) = s;                    % skewness
    index = index+1;
end



end

