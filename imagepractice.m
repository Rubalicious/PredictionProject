%% Basic image manipulation

I = imread('smileyface.jpg');
% imshow(I);
blackNwhite = im2bw(I);
% imshow(blackNwhite)
col = round(length(size(blackNwhite, 1))/2);
row = find(blackNwhite(:,col), 1 );
boundary = bwtraceboundary(blackNwhite, [row, col], 'N');
imshow(blackNwhite)
hold on
plot(boundary(:,2),boundary(:,1), 'ob')
hold off