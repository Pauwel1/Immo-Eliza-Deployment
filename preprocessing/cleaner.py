import pandas as pd
import numpy as np

class Preprocess:

    def clean(self, df = pd.DataFrame, isTrainingSet = bool) -> pd.DataFrame:
        """
        This method will clean the dataframe deleting duplicated rows,
        fixing errors, eliminating outliers.
        :param df: dataframe to clean
        """
        self.df = df

        # We clean first all the entirely empty rows
        self.df.dropna(how="all", inplace=True)

        # We delete the blank spaces at the beginning and end of each string
        self.df.apply(lambda x: x.strip() if type(x) == str else x)

        # Fixing errors
        # Fixing variable hasFullyEquippedKitchen
        has_hyperEquipped = self.df["kitchenType"].apply(
            lambda x: 1 if x == "HYPER_EQUIPPED" else 0
        )
        has_USHyperEquipped = self.df["kitchenType"].apply(
            lambda x: 1 if x == "USA_HYPER_EQUIPPED" else 0
        )
        self.df.hasFullyEquippedKitchen = (
            has_hyperEquipped | has_USHyperEquipped
        )

        # Deleting variable 'typeProperty', keeping 'subtypeProperty'
        del self.df["typeProperty"]

        # Dropping rows with price as NaN values
        self.df = self.df[self.df["price"].notna()]
        self.df = self.df[self.df["area"].notna()]

        # Dropping duplicated values
        self.df = self.df.drop_duplicates(
            subset=["area", "price"], keep="last"
        )

        if isTrainingSet == True:
            # cleaning features with less than 5 occurrences
            features = [
                "postalCode",
                "facadeCount",
                "subtypeProperty",
                "BedroomsCount",
            ]
            for feature in features:
                self.df = self.df[
                    self.df[feature].map(self.df[feature].value_counts()) > 5
                ]

        # Dropping outliers
        self.df = self.df[self.df["price"] < 6000000]
        self.df = self.df[self.df["area"] < 1350]

        # Creating new variable adding outside surface
        self.df.terraceSurface.fillna(0, inplace=True)
        self.df.gardenSurface.fillna(0, inplace=True)
        self.df["outsideSpace"] = (
            self.df["terraceSurface"] + self.df["gardenSurface"]
        )

        # Filling nan values to 0 for facadeCount
        self.df.facadeCount.fillna(0, inplace=True)

        # Deleting least correlated, reformatted and constant columns
        self.df = self.df.drop(
            [
                "kitchenType",
                "typeSale",
                "subtypeSale",
                "terraceSurface",
                "isFurnished",
                "gardenSurface",
            ],
            axis=1,
        )

        # Transform  variables into features
        features = [
            "postalCode",
            "buildingCondition",
            "subtypeProperty",
            "fireplaceExists",
            "hasSwimmingPool",
            "hasGarden",
            "hasTerrace",
            "hasFullyEquippedKitchen",
        ]
        for feature in features:
            cv_dummies = pd.get_dummies(self.df[feature])
            if cv_dummies.columns.__len__() < 3:
                cv_dummies.columns = [feature + "True", feature + "False"]
            self.df = pd.concat([self.df, cv_dummies], axis=1)
            del self.df[feature]

        return self.df.reset_index(drop=True)

    def rescale(self, df = pd.DataFrame):
        """This static method will standardize some of the features,
        all the areas (square meter) will be rescaled into their square root
        and the price into its logarithm
        :param df: cleaned data frame to resale
        :return: rescaleded dataframe
        """
        self.df = df

        df["price"] = np.log(df["price"])
        df["area"] = np.sqrt(df["area"])
        df["outsideSpace"] = np.sqrt(df["outsideSpace"])
        df["landSurface"] = np.sqrt(df["landSurface"])

        return df

    def adjustToTrainedModel(self, df = pd.DataFrame, isTrainingSet = False):
        """
        This method fit the new data into the format of the X dataset from
         the model to be able to predict using the model of the regressor
        :param df: new dataframe to fit into the X format.
        :return: None
        """

        if isTrainingSet == False:

            # We create a new data frame with the columns of the dataframe used to
            # train the model
            self.newData = pd.DataFrame(columns=self.df.columns.to_list())

            # We append our new data to this dataframe
            self.newData = self.newData.append(df)

            # Fill all the nan values with zeros
            self.newData.fillna(0, inplace=True)