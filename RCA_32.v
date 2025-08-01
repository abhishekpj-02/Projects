// 32-bit Ripple Carry Adder with Full Adder module

module RCA_32(output [31:0] sum, output cout, input [31:0] a, b);

  wire [31:0] c;
  assign c[0] = 0;

  FA fa0(sum[0], c[1], a[0], b[0], c[0]);
  FA fa[30:1](sum[30:1], c[31:2], a[30:1], b[30:1], c[30:1]);
  FA fa31(sum[31], cout, a[31], b[31], c[31]);

endmodule

module FA(output sum, cout, input a, b, c);

  assign sum = a ^ b ^ c;
  assign cout = (a ^ b) & c | (a & b);

endmodule

// Testbench for 32-bit RCA

module RCA_32_tb;

  wire [31:0] sum;
  wire cout;
  reg [31:0] a, b;
  reg cin;

  RCA_32 rca32(sum, cout, a, b);

  initial begin
    $display("a                             | b                             || cout | sum");
    $monitor("%b | %b || %b | %b", a, b, cout, sum);
  end

  initial begin
    a = 32'b10100000101000001111111111111111; 
    b = 32'b10100000101111111111111111100000;
    cin = 0;
    #10;

    a = 32'b01011000111111111111111111110100; 
    b = 32'b11110100111101001111111111111111;
    cin = 0;
    #10;

    a = 32'b11111111111111110000111100111101; 
    b = 32'b00001111000011111111111111111111;
    cin = 0;
    #10;

    a = 32'b11011111111111111110100011001010; 
    b = 32'b11001111111111111111100011001010;
    cin = 0;
    #10;
  end

endmodule

