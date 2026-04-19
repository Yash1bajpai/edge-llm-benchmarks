#!/bin/bash
# ============================================
# Edge LLM Benchmark Script
# Usage: bash scripts/run_benchmark.sh <model_path> <model_name>
# Example: bash scripts/run_benchmark.sh models/TinyLlama-FP16.gguf FP16
# ============================================

MODEL_PATH=$1
MODEL_NAME=$2
SEED=42
MAX_TOKENS=150
BINARY="./build/bin/llama-cli"

if [ -z "$MODEL_PATH" ] || [ -z "$MODEL_NAME" ]; then
  echo "Usage: bash scripts/run_benchmark.sh <model_path> <model_name>"
  exit 1
fi

echo "======================================"
echo " Edge LLM Benchmark — $MODEL_NAME"
echo "======================================"

echo ""
echo "--- Prompt 1: Logic & Reasoning ---"
$BINARY -m $MODEL_PATH --single-turn --seed $SEED -n $MAX_TOKENS \
  -p "Jane has 3 brothers. Each of her brothers has 2 sisters. How many sisters does Jane have? Think step-by-step."

echo ""
echo "--- Prompt 2: JSON Formatting ---"
$BINARY -m $MODEL_PATH --single-turn --seed $SEED -n $MAX_TOKENS \
  -p "Extract the core problem and the proposed solution from this text: 'Our server costs increased by 40% due to unoptimized database queries holding connections open. To fix this, we will implement a connection pool.' Output the result strictly as a valid JSON object with keys 'problem' and 'solution'. Do not add any other text."

echo ""
echo "--- Prompt 3: Constraint Adherence ---"
$BINARY -m $MODEL_PATH --single-turn --seed $SEED -n $MAX_TOKENS \
  -p "Write a polite 2-sentence email declining a meeting invite. You must start the first sentence with the word 'Unfortunately' and the second sentence with the word 'However'."

echo ""
echo "--- Prompt 4: Reading Comprehension ---"
$BINARY -m $MODEL_PATH --single-turn --seed $SEED -n $MAX_TOKENS \
  -p "Summarize the following in exactly 15 words: 'The James Webb Space Telescope is an infrared space observatory that launched on December 25, 2021, from Kourou, French Guiana, and arrived at the Sun-Earth L2 Lagrange point in January 2022.'"

echo ""
echo "--- Prompt 5: Creativity & Tone ---"
$BINARY -m $MODEL_PATH --single-turn --seed $SEED -n $MAX_TOKENS \
  -p "You are a highly sarcastic, grumpy old sailor. Explain what a smartphone is in exactly 3 sentences."

echo ""
echo "======================================"
echo " Benchmark Complete — $MODEL_NAME"
echo "======================================"
