# This is a line of comment
# Exemples of variables
first_variable <- 'this is an variable'
second_variable <- 12.5

#Vetores
vec_1 <- c(13,45.5,70.1,51,101)
vec_1

#Nomeação de Vetores

x <- c(1, 2, 3, 4)
names(x) <- c("Ricadro", "José", "Martin", "Jesualdo")

#Listas

ls <- list("a", 1L, 1.5, TRUE)
str_ls <- str(list("a", 1L, 1.5, TRUE))

#Nomeação de Listas
ls <- list("Rio de Janeiro"=1, "São Paulo"=2, "Espírito Santo"=3)

#Pacotes

install.packages("tidyverse")
library(tidyverse)
library(lubridate)

#Datas e Horas
today()
now()

#String to date
ymd("2023-11-23")
mdy("September 23th, 2023")
dmy("23-Sep-2023")
ymd(20231123)

#Date-time

ymd_hms("2023-11-23 16:48:00")
mdy_hms("11-23-2023 16:49:55")

#Date-Time to Date
as_date(now())

#Data Frame
data <- data.frame(x = c(1, 2, 3) , y = c(1.5, 5.5, 7.5))

#Files / Arquivos
dir.create("beligol")   #Criando diretório

file.create("teste.txt")  # Criando Arquivo

file.copy("teste.txt","beligol/")   #Copiando arquivo

unlink("teste.txt")   #Excluindo Arquivo

#Matrizes
matx <- matrix(c(1:10),nrow = 2)
maty <- matrix(c(1:10),ncol = 2)

# Operadores Aritiméticos

sales_1 <- 35657.98
sales_2 <- 43810.5
midyear_sales <- sales_1 + sales_2
year_sales <- midyear_sales * 2

# Functions

xquadrado <- function(x){
  return(x^2)
}

xquadrado(2)

# Pipes
data('ToothGrowth')
view((ToothGrowth))

filter_toothGrow <- ToothGrowth %>%
  filter(dose==0.5) %>%
  group_by(supp) %>%
  summarize(mean_lean = mean(len, na.rm = T), .group = "drop")

x <- c(4,4,4,4)

x %>% sum() %>% sqrt()

y <- 5

y %>% xquadrado()

# Data Frames

nomes <- c("Davi", "Lannes", "Yan", "Kaio")
num_camisa <- c(14,11,9,5)
escalacao <- data_frame(nomes,num_camisa)

# Import Data
champions <- read_csv("DATABASE - DataBase.csv") %>% select('Champion')

# Limpeza de Dados

id <- c(1:10)
nome <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", "Christy Hickman", "Johnson Harper", "Candace Miller", "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia")

id_cargo <- c("Profissional", "Programador", "Gerencia", "Administrativo", "Desenvolvedor", "Programador", "Gerencia", "Administrativo", "Desenvolvedor", "Programador")

empregado <- data.frame(id, nome, id_cargo)

separate(empregado, nome, into = c("Nome", "Sobrenome"), sep = " ")

#Visualização de Dados

          #____________ Gráficos de Disperssão __________________

#ggplot(data=<DATA>)+<GEOM_FUNCTION>(mapping= aes(<ASTHETIC MAPPINGS>))

ggplot(data=penguins) +geom_point(mapping = aes(x=bill_length_mm, y=bill_depth_mm))

ggplot(data=penguins) +geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species)) # Color

ggplot(data=penguins) +geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, shape=species)) # Shape

ggplot(data=penguins) +geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species, shape=species)) # Formato

ggplot(data=penguins) +geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species, size=species)) # Tamanho

ggplot(data=penguins) +geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, alpha=species)) # Alpha

ggplot(data=penguins) +geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, alpha=species),color="red") # Cor


#__________________________________Tipos de Gráficos__________________________________

    # Curva Suave
ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm, y=body_mass_g))

    # Multiplias curvas suaves
ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm, y=body_mass_g, linetype=species))

    # Sobreposição de Gráficos
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g))+
  geom_smooth(mapping = aes(x=flipper_length_mm, y=body_mass_g))

    # GRáfico de Disperssão com ruido
ggplot(data=penguins)+
  geom_jitter(mapping = aes(x=flipper_length_mm, y=body_mass_g))

    # Gráfico de Barras
ggplot(data=diamonds)+
  geom_bar(mapping = aes(x=cut, fill=clarity))

#__________________________________Facetas de Gráficos__________________________________

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species))+
  facet_wrap(~species)

ggplot(data=diamonds)+
  geom_bar(mapping = aes(x=color, fill=cut))+
  facet_wrap(~cut)

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species))+
  facet_grid(sex~species)

              #____________ Títulos e Anotações __________________

plot <- ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species))+
  labs(title="Palmer Penguins: Bosy Mass vs. Flipper Lenght", subtitle = "Sample of three species",
       caption = "Dr. Karen")+
  annotate("text", x=220, y=3500, label="The Gentoos area the largest", color="purple",
           fontface= "bold", size=4.5, angle=25)
plot+
  annotate("text", x=220, y= 3500, label="The gentoo are the largest")

# Salvando Plots
ggsave("Three Penguins Species.png")

      #____________ PNG ____________

png(file = "exampleplot.png", bg = "transparent")
plot(1:10)
rect(1, 5, 3, 7, col = "white")
dev.off()

      #____________ PNG ____________

pdf(file = "example.pdf",    
    width = 4,     
    height = 4) 
plot(x = 1:10,     
     y = 1:10)
abline(v = 0)
text(x = 0, y = 1, labels = "Random text")
dev.off()
