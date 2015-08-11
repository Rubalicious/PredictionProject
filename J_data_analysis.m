%% Read all the pictures into a data space


%Make a table of the stats
table = zeros(40,5);
%making columns that are: ID, brightness, contrast, range, avg grayness

%reading happiness/sadness folders
happy = dir('/home/jose/Documents/MATLAB/PredictionProject/picture data/happy*');
sad   = dir('/home/jose/Documents/MATLAB/PredictionProject/picture data/sad*');
cd('/home/jose/Documents/MATLAB/PredictionProject/picture data');

H = happy';
S = sad';

while i < 21;
    
    rgbH = imread(H(i).name);
    rgbS = imread(S(i).name);
    
    brightnessH = mean2(H(i).name);
    brightnessS = mean2(S(i).name);
    
    contrastH = std2(H(i).name);
    contrastS = std2(S(i).name);
    
    rangeH = max(H(i).name)-min(H(i).name);
    rangeS = max(S(i).name)-min(S(i).name);
    
    grayH = rgb2gray(rgbH);
    grayS = rgb2gray(rgbS);
    
    avggrayH = mean2(grayH);
    avggrayS = mean2(grayS);
    
    %populating table
    table(i,1) = i;
    table(i,2) = brightnessH;
    table(i,3) = contrastH;
    table(i,4) = rangeH;
    table(i,5) = avggrayH;
    
    table(j,1) = j;
    table(j,2) = brightnessS;
    table(j,3) = contrastS;
    table(j,4) = rangeS;
    table(j,5) = avggrayS;
    
    j = j+1;
    i = i+1;
end

disp(table)

