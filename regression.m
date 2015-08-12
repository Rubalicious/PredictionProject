%% Read all the pictures into a data space

%Make a table of the stats
table = zeros(40,5);
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
    
    %populating table
    table(i,1) = i;
    table(i,2) = brightness;
    table(i,3) = contrast;
    table(i,4) = range;
    table(i,5) = avggray;
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
    
    %populating table
    table(i,1) = i;
    table(i,2) = brightness;
    table(i,3) = contrast;
    table(i,4) = range;
    table(i,5) = avggray;
    i = i+1;
end