% Secant root finder

THRESHOLD = 0.0001;
MAX_TRIES = 100;
guess_a = -1;
guess_b = 1;

i = 0;
while i < MAX_TRIES
    % calculate slope here to simplify equation
    slope = (f(guess_b) - f(guess_a)) / (guess_b - guess_a);
    % next guess comes from the intersection of the secant line & x-axis
    guess_c = guess_b - (f(guess_b) / slope);
    
    % if our f(guess_c) is within the THRESHOLD of zero we are finished
    if (f(guess_c) > 0 - THRESHOLD) && (f(guess_c) < 0 + THRESHOLD)
        disp(f(guess_c))
        disp(guess_c)
        disp(i)
        disp('finished')
        break
    end
    
    % always take new guess as input for the next iteration, remove old.
    guess_a = guess_b;
    guess_b = guess_c;
    i = i+1;
end