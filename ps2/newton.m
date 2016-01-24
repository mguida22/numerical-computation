% Newton root finder

THRESHOLD = 0.0001;
MAX_TRIES = 100;
guess_a = -1;

i = 0;
while i < MAX_TRIES
    % cos(x) is the derivative, we could make MATLAB calculate this but it
    % isn't necessary if we already know it.
    %
    % next guess comes from the intersection of the secant line & x-axis
    guess_b = guess_a - (f(guess_a) / cos(guess_a));
    
    % if our f(guess_b) is within the THRESHOLD of zero we are finished
    if (f(guess_b) > 0 - THRESHOLD) && (f(guess_b) < 0 + THRESHOLD)
        disp(f(guess_b))
        disp(guess_b)
        disp(i)
        disp('finished')
        break
    end
    
    % always take new guess as input for the next iteration, remove old.
    guess_a = guess_b;
    i = i+1;
end