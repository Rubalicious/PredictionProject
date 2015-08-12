function x = getKurtosis(I)
   
    A = zeros(1,size(I,1)*size(I,2));
    i = 1;
    for r = 1:size(I,1)
        for c = 1:size(I,2)
            A(1,i) = I(r,c);
            i = i+1;
        end
    end
    x = kurtosis(A);
end