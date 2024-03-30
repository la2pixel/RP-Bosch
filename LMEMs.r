# Load required packages
library(lme4)
library(sjstats)



##Exposure order for each participant along with subjective experiences were mapped using Excel

file_path <- "C:/Users/Lalitha Sivakumar/Desktop/analysis_lalitha/CMS- internship/STANDARDIZED.xlsx"
df_std <- read_excel(file_path)
head(df_std)


##############################################################################################################################
#Example model -> VALENCE

# mod0<- fixed intercept + fixed effects + random intercept for participants
mod0 <- lmer(pdelt ~ ord + age + autexp + valence + (1 | vp), data = df_std)

# Fit Linear Mixed Model with Random Intercept and Random Slope
mod1 <- lmer(pdelt ~ ord + age + autexp + valence + (1 + time_index | vp), data = df_std)

# fixed intercept and random slope removed
mod2 <- lmer(pdelt ~ -1+ord + age + autexp + valence + (1 | vp), data = df_std)

# fixed effect valence removed (was insignificantin mod0)
mod3 <- lmer(pdelt ~ ord + autexp + age + (1 | vp), data = df_std)

anova(mod0,mod1,mod2,mod3)

# Best performing model: mod0
summary_lmm <- summary(mod0)

summary(mod0) #FE and RE

# Extract variance components
covrand<-as.data.frame(VarCorr(mod0))

sigma0<- covrand[1,4]
sigmaeps<-covrand[2,4]

# Inter-individual variability measure
ICC <- sigma0 / (sigma0 + sigmaeps)
print(ICC)

