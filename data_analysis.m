%% Read all the pictures into a data space


%Make a table of the stats
table = zeros(40,5);
%making columns that are: ID, brightness, contrast, range, avg grayness
%reading happiness folder
files = dir('picture data/happiness/*.jpg');
i = 1;
for file = files'
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

scatter3(table(21:40,2), table(21:40,3), table(21:40,4),'ob');
hold off
xlabel('brightness')
%% some ideas
%notice the difference between average grayness
plot(table(1:20,5))
hold on
plot(table(21:40,5))
xlabel('picture ID')
ylabel('average grayness')
legend('happy pictures', 'sad pictures')
hold off
%% plot the average of happy pictures and sad pictures
hold on
x = 1:20;
y1 = mean(table(1:20,5));
scatter(x,y1*ones(20,1),'b*');
y2 = mean(table(21:40,5));
scatter(x, y2*ones(20,1),'r');
hold off