function x = getMedian(M)
    A = zeros(1,size(M,1)*size(M,2));
    i = 1;
    for r = 1:size(M,1)
        for c = 1:size(M,2)
            A(1,i) = M(r,c);
            i = i+1;
        end
    end
    x = kurtosis(A);
end