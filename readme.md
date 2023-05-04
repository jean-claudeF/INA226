# INA226 Micropython library (not ready yet!)
This lib is based on the one that Chris Becker designed:
https://github.com/elschopi/TI_INA226_micropython

I have added functions to directly read the voltage and current registers for debugging, and corrected the shunt voltage resolution that, according to the datasheet is 2.5uV.

My results however are WRONG, and help would be appreciated very much.

The error seems to be already in the shunt voltage register values.

Example:
For I = 1A and a shunt of 0.002 Ohms I should have a shunt voltage of 2mV (Measured with a DMM, is OK).
With an LSB of 2.5uV, the register should read 2000uV/2.5uV = 800
The value I read is ca. 2000 however.
What's wrong here???

