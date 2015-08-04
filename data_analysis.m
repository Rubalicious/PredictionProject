%% Read all the pictures into a data space


%Make a table of the stats
table = zeros(40,4);
%making columns that are: ID, brightness, contrast, avg grayness
%reading happiness folder
files = dir('picture data/happiness/*.jpg');
i = 1;
for file = files'
    imread(file.name);
    brightness = mean2(file.name);
    contrast = std(file.name);
    range = max(file.name)-min(file.name);
    
    %populating table
    table(i,1) = i;
    table(i,2) = brightness;
    table(i,3) = contrast;
    table(i,4) = range;
    i = i+1;
end
figure
scatter3(table(:,2), table(:,3), table(:,4),'*r');
xlabel('brightness')
ylabel('contrast')
zlabel('range')
%% sadness
%reading sadness folder
files = dir('picture data/sadness/sad*');
i = 21;
for file = files'
    imread(file.name);
    brightness = mean2(file.name);
    contrast = std(file.name);    
    range = max(file.name)-min(file.name);
    
    %populating table
    table(i,1) = i;
    table(i,2) = brightness;
    table(i,3) = contrast;
    table(i,4) = range;
    i = i+1;
end
hold on
scatter3(table(:,2), table(:,3), table(:,4),'ob');
hold off
xlabel('brightness')
ylabel('contrast')
zlabel('range')