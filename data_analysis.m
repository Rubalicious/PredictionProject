%% Read all the pictures into a data space

%Make a table of the stats
table = zeros(40,15);
%making columns that are: ID, brightness, contrast, range, avg grayness
%reading happiness folder
files = dir('picture data/happiness/*.jpg');
i = 1;
for file = files'
    rgb = imread(file.name);
    average = mean2(file.name);
    stdev = std2(file.name);
    range = max(file.name)-min(file.name);
    gray = rgb2gray(rgb);
    avggray = mean2(gray);
    graymode = mode(mode(gray));
    rmode = mode(mode(rgb(:,:,1)));
    gmode = mode(mode(rgb(:,:,2)));
    bmode = mode(mode(rgb(:,:,3)));
    fvec = quantile(rgb,0.25);
    fquantile = squeeze(quantile(fvec,0.25));
    svec = quantile(rgb,0.5);
    squantile = squeeze(quantile(fvec,0.5));
    tvec = quantile(rgb,0.75);
    tquantile = squeeze(quantile(fvec,0.75));
    
    
    %populating table
    table(i,1) = i;                     % ID
    table(i,2) = average;               % average color
    table(i,3) = stdev;                 % standard deviation
    table(i,4) = range;                 % range
    table(i,5) = min(file.name);        % minimum value
    table(i,6) = max(file.name);        % maximum value
    table(i,7) = avggray;               % average grayness
    table(i,8) = graymode;              % most common gray color
    table(i,9) = rmode;                 % most common red color
    table(i,10) = gmode;                % most common green color
    table(i,11) = bmode;                % most common blue color
    table(i,12) = fquantile(1);         % first quantile
    table(i,13) = squantile(1);         % second quantile (median)
    table(i,14) = tquantile(1);         % third quantile
    i = i+1;
end
figure
hold on
scatter3(table(1:20,2), table(1:20,3),table(1:20,4),'*r');
xlabel('brightness')
ylabel('contrast')
zlabel('range')
%% sadness
%reading sadness folder
files = dir('picture data/sadness/sad*');
i = 21;
for file = files'
    rgb = imread(file.name);
    average = mean2(file.name);
    stdev = std2(file.name);
    range = max(file.name)-min(file.name);
    gray = rgb2gray(rgb);
    avggray = mean2(gray);
    graymode = mode(mode(gray));
    rmode = mode(mode(rgb(:,:,1)));
    gmode = mode(mode(rgb(:,:,2)));
    bmode = mode(mode(rgb(:,:,3)));
    fvec = quantile(rgb,0.25);
    fquantile = squeeze(quantile(fvec,0.25));
    svec = quantile(rgb,0.5);
    squantile = squeeze(quantile(fvec,0.5));
    tvec = quantile(rgb,0.75);
    tquantile = squeeze(quantile(fvec,0.75));
    
    
    %populating table
    table(i,1) = i;                     % ID
    table(i,2) = average;               % average color
    table(i,3) = stdev;                 % standard deviation
    table(i,4) = range;                 % range
    table(i,5) = min(file.name);        % minimum value
    table(i,6) = max(file.name);        % maximum value
    table(i,7) = avggray;               % average grayness
    table(i,8) = graymode;              % most common gray color
    table(i,9) = rmode;                 % most common red color
    table(i,10) = gmode;                % most common green color
    table(i,11) = bmode;                % most common blue color
    table(i,12) = fquantile(1);         % first quantile
    table(i,13) = squantile(1);         % second quantile (median)
    table(i,14) = tquantile(1);         % third quantile
    i = i+1;
end

scatter3(table(21:40,2), table(21:40,3), table(21:40,4),'ob');
hold off
xlabel('brightness')
%% some ideas
%notice the difference between average grayness
figure
plot(table(1:20,7))
hold on
plot(table(21:40,7))
xlabel('picture ID')
ylabel('average grayness')
legend('happy pictures', 'sad pictures')
hold off
%% plot the average of happy pictures and sad pictures
hold on
x = 1:20;
y1 = mean(table(1:20,7));
scatter(x,y1*ones(20,1),'b*');
y2 = mean(table(21:40,7));
scatter(x, y2*ones(20,1),'r');
hold off