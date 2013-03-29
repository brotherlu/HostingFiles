function [Vto,Lto,Dto,Amean,SG,VClimb,Vcruise,TurnRate] = fcn(Wto,b,S,AR,TR,PropThrust,SweepLE)
 
%Flight Parameters
Rhoto = 0.00227; 
Rhocruise = 0.002176; 
G = 32.2; 
%Airplane Parameter
Cfe = 0.0055; 
Fc = 0.03; 
%Surface Area of fuselage only obtained through XFLR5 [ft^2]
Sfuselage = 3.11/144; 
Cl2d = 1.3294;
SweepMaxt = 24.10;
AoA = 10;
AReff = 1.2*AR;
SweepQuarter = sweep(SweepLE,TR,AR);
Cl3d = cl3d(SweepQuarter,Cl2d);
Clmaxto = clto(Cl3d); 
Clmin = 0.5368; 
%Take off Velocity
Vto = vto(Wto,S,Rhoto,Clmaxto);
%Exposed Surface
Sexposed = sexp(S,Sfuselage);
Cmac = cm(S,b);
%Calculation of Take Off Drag Coeff
e = 1.78*(1-(0.045*(AR^0.68)))-0.64;
K = k(AReff,e);
CDo = cdo(Cfe,S,Sexposed);
CDi = cdi(K,Clmin);
CDto = cdto(CDo,CDi);
%Calculation of Mean Take off Acceleration
Lto = lto(Rhoto,S,Clmin,Vto);
Dto = dto1(Rhoto,S,CDto,Vto);
Amean = amean(G,Wto,PropThrust,Dto,Fc,Lto);
%Calculation of Take Off Distance
SG = sg(Vto,Amean);
% Climb Rate
VClimb = vclimb(PropThrust,Dto,Wto,Vto);
%Calculation of Wing Lift Slope & Cruise Lift Coefficient
Mach = mach(Vto);
Beta2 = beta2(Mach);
F = 0.98;
AirfoilE = 0.95; % based on Raymer
CLalfa = calalfa(AReff,Beta2,AirfoilE,SweepMaxt,Sexposed,S,F);
CLcruise = clcruise(CLalfa,AoA);
%Claculation of Cruise Velocity, Thrust & Lift
Vcruise = vcruise(Wto,Rhocruise,CLcruise,S);
%Turn Rate
LoadF = 1.3; %Assume a load factor based on Raymers
TurnRate = tr(G,LoadF,Vcruise);
 
function SweepQuarter = sweep(SweepLE,TR,AR)
SweepQuarter = atan(tan(SweepLE)-((1-TR)/AR*(1+TR)));
function Cl3d = cl3d(SweepQuarter,Cl2d)
Cl3d = 0.9*Cl2d*cos(SweepQuarter);
function Clmaxto = clto(Cl3d)
Clmaxto = Cl3d*0.8
function Vto = vto(Wto,S,Rhoto,Clmaxto)
Vto = ((2*Wto)/(S*Rhoto*Clmaxto))^0.5; 
function Sexposed = sexp(S,Sfuselage)
Sexposed = S - Sfuselage;
function Cmac = cm(S,b)
Cmac = S/b; 
function CDo = cdo(Cfe,S,Sexposed)
CDo = Cfe*(Sexposed/S); 
function K = k(AReff,e)
K = 1/(pi*AReff*e);
function CDi = cdi(K,Clmin)
CDi = K*(Clmin^2); 
function CDto = cdto(CDo,CDi)
CDto = CDo + CDi; 
function Lto = lto(Rhoto,S,Clmin,Vto)
Lto = 0.5*Rhoto*S*Clmin*(0.7*Vto^2); 
function Dto = dto1(Rhoto,S,CDto,Vto)
Dto = 0.5*Rhoto*S*CDto*(0.7*Vto^2); 
function Amean = amean(G,Wto,PropThrust,Dto,Fc,Lto)
Amean = (G/Wto)*(PropThrust-Dto-Fc*(Wto-Lto)); 
function SG = sg(Vto,Amean)	
SG = (0.7*(Vto^2))/(2*Amean); 
function VClimb = vclimb(PropThrust,Dto,Wto,Vto)
VClimb = ((PropThrust - Dto)/Wto)*Vto;
function Mach = mach(Vto)
Mach = (Vto)/1126; 
function Beta2 = beta2(Mach)
Beta2 = 1-(Mach^2);
function CLalfa = calalfa(AReff,Beta2,AirfoilE,SweepMaxt,Sexposed,S,F)
CLalfa = ((2*pi*(AReff))/(2+((4 +(((AReff)^2*Beta2)/AirfoilE^2)*(1 +(tan(SweepMaxt)^2/Beta2)))^0.5)))*(Sexposed/S)*F; 
function CLcruise = clcruise(CLalfa,AoA)
CLcruise = CLalfa*AoA; 
function Vcruise = vcruise(Rhocruise,CLcruise,Wto,S)
Vcruise = ((2/(Rhocruise*CLcruise))*(Wto/S))^0.5; 
function TurnRate = tr(G,LoadF,Vcruise)
TurnRate = ((G*((LoadF^2)-1)^0.5)/Vcruise)*57.3;

%%%%%%%%%%%%%%END%%%%%%%%%%%%%%%%%
