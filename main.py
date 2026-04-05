#!/usr/bin/env python3

from src.agent import create_chain


def main():
    print("Agricultural Fertilizer Recommendation Agent")
    print("Enter the following details for fertilizer recommendations:\n")

    try:
        ph = float(input("Soil pH level: "))
        n = input("Nitrogen level (low/medium/high): ").strip().lower()
        p = input("Phosphorus level (low/medium/high): ").strip().lower()
        k = input("Potassium level (low/medium/high): ").strip().lower()
        crop = input("Crop type (e.g., corn, wheat): ").strip().lower()

        chain, knowledge = create_chain()
        result = chain.invoke(
            {
                "knowledge": knowledge,
                "ph": ph,
                "n": n,
                "p": p,
                "k": k,
                "crop": crop,
            }
        )
        print("\nFertilizer Recommendation:")
        print(result)
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number for pH.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
