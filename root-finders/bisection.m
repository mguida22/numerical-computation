% Bisection root finder
% Initial guesses must bracket root

THRESHOLD = 0.0001;
MAX_TRIES = 100;
guess_a = -1;
guess_b = 1;

i = 0;
while i < MAX_TRIES
    midpoint = (guess_a + guess_b) / 2;
    
    % calculate f(midpoint) once so we can reuse instead of recalculate
    f_midpoint = f(midpoint);
    
    % if our f(midpoint) is within the THRESHOLD of zero we are finished
    if (f_midpoint > 0 - THRESHOLD) && (f_midpoint < 0 + THRESHOLD)
        disp(f_midpoint)
        disp(midpoint)
        disp(i)
        disp('finished')
        break
    end
    
    % check the sign of f(guess_a) vs f(midpoint) and set midpoint
    % accordingly. We always need to bracket the root so we need a (+)(-)
    if (f(guess_a)) * (f_midpoint > 0) < 0
        guess_b = midpoint;
    else
        guess_a = midpoint;
    end
    
    i = i+1;
end