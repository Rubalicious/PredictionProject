%% Read all the pictures into a data space

%Make a table of the stats
table = zeros(40,7);
%making columns that are: ID, brightness, contrast, range, avg grayness

%reading happiness folder
files = dir('picture data/happiness/*.jpg');
i = 1;

for file = files'
    
    %getting image statistics
    rgb = imread(file.name);
    brightness = mean2(file.name);
    contrast = std2(file.name);
    range = max(file.name)-min(file.name);
    gray = rgb2gray(rgb);
    avggray = mean2(gray);
    skewness = getSkewness(rgb);
    kurtosis = getKurtosis(rgb);
    
    %populating table
    table(i,1) = 1;
    table(i,2) = brightness;
    table(i,3) = contrast;
    table(i,4) = range;
    table(i,5) = avggray;
    table(i,6) = skewness;
    table(i,7) = kurtosis;
    i = i+1;
end

%% sadness
%reading sadness folder
files = dir('picture data/sadness/sad*');

for file = files'
    
    %getting image statistics
    rgb = imread(file.name);
    brightness = mean2(file.name);
    contrast = std2(file.name);    
    range = max(file.name)-min(file.name);
    gray = rgb2gray(rgb);
    avggray = mean2(gray);
    skewness = getSkewness(rgb);
    kurtosis = getKurtosis(rgb);
    
    %populating table
    table(i,1) = 2;
    table(i,2) = brightness;
    table(i,3) = contrast;
    table(i,4) = range;
    table(i,5) = avggray;
    table(i,6) = skewness;
    table(i,7) = kurtosis;
    i = i+1;
end

%% Regression Model
 disp(table)
 
 HappyOrSad = table(:,1);
 
 [B,dev,stats] = mnrfit(table(:,2:end),HappyOrSad);
 
 disp(B)
